#Kris Hanks
#Homework 4, COE332
import math
import requests
import xmltodict
import xml.etree.ElementTree as ET
import urllib.request
from flask import Flask, request

app = Flask(__name__)

#Load in data
url = "https://nasa-public-data.s3.amazonaws.com/iss-coords/current/ISS_OEM/ISS.OEM_J2K_EPH.xml"
response = requests.get(url)
with open('ISS.OEM_J2K_EPH.xml', 'wb') as data:
    data.write(response.content)
tree = ET.parse('ISS.OEM_J2K_EPH.xml')
root = tree.getroot()

ISS_VALUES = []

#Get a list of all epochs in data set
def find_the_EPOCHS() -> dict:
    """
    Get a list of all epochs, state vectors, and velocities in the data set from ISS.OEM_J2K_EPH.xml.

    Returns:
    Dictionary containing all epochs, state vectors, and velocities in the data set. 
    """
    global ISS_VALUES
    position = root.findall('.//stateVector')
    for position in position:
        epochs = position.find("EPOCH").text
        x = position.find('X').text
        x_dot = position.find('X_DOT').text
        y = position.find('Y').text
        y_dot = position.find('Y_DOT').text
        z = position.find('Z').text
        z_dot = position.find('Z_DOT').text
        ISS_VALUES.append({
            'EPOCH' : epochs,
            'x' : x,
            'x_dot': x_dot,
            'y' : y,
            'y_dot': y_dot,
            'z' : z,
            'z_dot' : z_dot})
    return { 'ISS_VALUES' : ISS_VALUES}

#Help route to return readable strong with brief descriptions of available routes & methods.
@app.route('/help', methods = ['GET'])
def api_help():
    """
    Returns a list of all available routes, their mehtods, and docstrings.
    """
    output = 'Available routs and methods: \n'
    for route in app.url_map.iter_rules():
        if route.endpoint != 'static':
            methods = ','.join(route.methods)
            output += f'{route.rule} [{methods}]\n'
            if route.endpoint:
                func = app.view_functions[route.endpoint]
                output += f'{func.__doc__}\n\n'

    return output

#Route to return data set
@app.route('/', methods = ['GET'])
def get_mydata() -> dict:
    """
    Returns all the epochs, state vectors, and velocities in the data set.

    Returns:
    Dictionary containing all epochs, state vectors, and velocities in the data set. 
    """
    return find_the_EPOCHS()

#Route ('/epochs') to return a list of all epochs in the data set
@app.route('/epochs', methods = ['GET'])
def get_epochs() -> dict:
    """
    Returns a list of only the epochs in the data set. 

    Returns:
    Dictionary of all epochs in the data set. 
    """
    epochcheck = find_the_EPOCHS()['ISS_VALUES']
    offset = request.args.get('offset', default=0, type=int)
    limit = request.args.get('limit', default=len(epochcheck), type=int)

    epochs_data = find_the_EPOCHS()['ISS_VALUES']
    end_index = offset + limit

    epochs = [d['EPOCH'] for d in epochs_data[offset:end_index]]

    return {'epochs' : epochs}

#Route ('/epochs/<epochval>') to return a state vectors for a specific Epoch from the data set
@app.route('/epochs/<string:epochval>', methods = ['GET'])
def get_state_vectors(epochval:str) -> dict:
    """
    Returns a state vector for a specific epoch in the data set.

    Args:
    String, epochval - the epoch value specified by user used to return state vector. 

    Returns:
    Dictionary containing the state vector for the specified epoch value. 
    """
    for d in find_the_EPOCHS()['ISS_VALUES']:
        if 'EPOCH' in d and d['EPOCH'] == epochval:
            return {'state_vectors' :
                    {'x' : d['x'],
                     'x_dot': d['x_dot'],
                     'y' : d['y'],
                     'y_dot': d['y_dot'],
                     'z' : d['z'],
                     'z_dot' : d['z_dot']
                     }}
    return f"Error in get_state_vectors"


#Route ('/epochs/<epochval>/speed to return speed for a specific Epoch
@app.route('/epochs/<string:epochval>/speed',methods = ['GET'])
def get_speed(epochval:str) -> float:
    """
    Collects velocity vector for specified epoch value and calulates speed using the following equation:
    speed = sqrt(x_dot^2 + y_dot^2 + z_dot^2)

    Arguments:
    String, epochval - the epoch value specified by user used to return state vector. 

    Returns:
    Float, Speed - Speed of ISS at specified epoch value. 
    """
    for d in find_the_EPOCHS()['ISS_VALUES']:
         if 'EPOCH' in d and d['EPOCH'] == epochval:
             x_dot = d['x_dot']
             y_dot = d['y_dot']
             z_dot = d['z_dot']
    #Calculate Speed
    speed = math.sqrt((float(x_dot)**2)+(float(y_dot)**2)+(float(z_dot)**2))
    return {'speed': speed}

#Route to delete everything from the in-memory dictionary of ISS data.
@app.route('/delete-data', methods=['DELETE'])
def delete_data():
    """
    Delete all data from the dictionary object.
    """
    global ISS_VALUES
    ISS_VALUES = []
    global root
    root.clear()
    return "All data deleted successfully.\n"

@app.route('/post-data', methods = ['POST'])
def post_data():
    find_the_EPOCHS()
    return "Data restored.\n"

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
