import requests
import csv
import redis
import json
from flask import Flask, request, jsonify

app = Flask(__name__)

def get_redis_client():
    return redis.Redis(host='127.0.0.1', port=6379, db=0, decode_responses=True)
rd = get_redis_client()

#DATA ROUTE
@app.route('/data', methods=['POST', 'GET', 'DELETE'])
def load_data():
    """
    Load, read, or delete data from a Redis database.

    Returns:
        GET - A list of redis keys.
        POST/DELTE - A string message indicating success or failure. 

    """
    #POST - load the HGNC data to a Redis database
    if request.method == 'POST' : 
        url = "https://ftp.ebi.ac.uk/pub/databases/genenames/hgnc/json/hgnc_complete_set.json"
        response = requests.get(url)
        data = response.json()
        for item in data['response']['docs']:
            #Pull hgnc value to use as key
            hgnc_id = item.get('hgnc_id')
            if item is not None:
                for i in item:
                    if type(item[i]) == list:
                        item[i] = '|'.join(str(x) for x in item[i])
            rd.hset(hgnc_id, mapping = item)
        return 'Data loaded to Redis.\n'
    #GET - read all data out of Redis and return it as a JSON list
    elif request.method == 'GET':
        output_list = []
        for key in rd.scan_iter():
            output_list.append(rd.hgetall(key))
        return jsonify(output_list)

    #DELETE - delete all data from Redis
    elif request.method == 'DELETE':
       rd.flushdb()
       return 'Data deleted from Redis.\n'
    else:
       return 'The method you tried does not work.\n'
@app.route('/genes', methods = ['GET'])
def genes():
    """
    Return a json-formatted list of all hgnc_id fields.

    Returns:
    List of json-formatted hgnc_id fields. 
    """
    #Return a json-formatted list of all hgnc_id fields
    keys = rd.keys()
    data = []
    for key in keys:
        hgnc_id = rd.hget(key,'hgnc_id')
        if hgnc_id:
            data.append(hgnc_id)
    return jsonify(data)

@app.route('/genes/<string:hgnc_val>', methods = ['GET'])
def hgnc_id(hgnc_val):
    """
    Return all data associated with a given <hgnc_id>.
    """
    #Handle case where something other than a valid gene ID is rprovided by the user. 

    #return all data associated with a given <hgnc_id>
    data = rd.hgetall(hgnc_val)
    if not data:
        return f"No data found for hgnc_id {hgnc_val}\n"
    return jsonify(data)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
