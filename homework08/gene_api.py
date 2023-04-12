import requests
import csv
import redis
import matplotlib.pyplot as plt
import numpy as np
import json
import os
from flask import Flask, request , jsonify

app = Flask(__name__)

#Automatically return redis ip address
redis_ip = os.environ.get('REDIS_IP')
if not redis_ip:
    raise Exception('REDIS_IP enviornment variable not set\n')
print("Connecting to Redis at ", redis_ip)
rd = redis.Redis(host = redis_ip, port = 6379, db = 0)
rd_tab2 = redis.Redis(host = redis_ip, port = 6379, db = 1)


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
        keys = rd.keys()
        output_list = []
        for key in keys: 
            data = rd.hgetall(key)
            decoded_data = {k.decode('utf-8'): v.decode('utf-8') for k, v in data.items()}
            output_list.append(decoded_data)
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
            decoded_id = hgnc_id.decode('utf-8')
            data.append(decoded_id)
    return jsonify(data)

@app.route('/genes/<string:hgnc_val>', methods = ['GET'])
def hgnc_id(hgnc_val):
    """
    Return all data associated with a given <hgnc_id>.
    """
    #Handle case where something other than a valid gene ID is rprovided by the user. 

    #return all data associated with a given <hgnc_id>
    data = []
    value = rd.hgetall(hgnc_val)
    if not value:
        return f"No data found for hgnc_id {hgnc_val}\n"
    decoded_val = {k.decode('utf-8'): v.decode('utf-8') for k, v in value.items()}
    data.append(decoded_val)

    return jsonify(data)

@app.route('/image', methods = ['GET', 'POST', 'DELETE'])
def images():
    """
    """

    #Delete image
    if request.method == 'DELETE' :
      rd_tab2.delete('image')
      return 'Image deleted.\n'
    #Return Image to user
    elif request.method == 'GET' :
        get_image = rd_tab2.get('image')
        if not get_image:
            return 'No image found.\n'
        return send_file(io.BytesIO(get_image), mimetyoe = 'image/png')
    elif request.method == 'POST' :
        keys = rd.keys()
        if not keys:
            return 'No data available.\n'

        #Count how many genes with id 1987, 40, 465    
        plot_gene_id = ["1987", "40", "465", "other"]
        gene_id_count = [ 0, 0, 0, 0]
        percentage_gene_id = [0,0,0,0]
        count = 0
        for key in keys:
            value = rd.hget(key, 'gene_group_id')
            if value in plot_gene_id:
                index = plot_gene_id.index(value)
                gene_id_count[index] +=1
            else:
                gene_id_count[3] += 1 

        count = sum(gene_id_count)
        for i in gene_id_count:
            if i == 0 :
                percentage_gene_id.append(0)
            else:
            percentage_gene_id.append(i/ count)

        labels = [plot_gene_id[i] for i in range(len(percentage_gene_id))]

        values = [percentage_gene_id[i] for i in range(len(percentage_gene_id))]

        # Create pie chart
        fig, ax = plt.subplots()
        ax.pie(values, labels=labels, autopct='%1.1f%%', startangle=90)
        ax.axis('equal')
        ax.set_title('Gene Group ID Distribution')
        #Write resulting plot to database (db=1)
        image = fig.canvas.tostring_rgb()
        rd_tab2.set('gene_group_pie_chart', image)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
