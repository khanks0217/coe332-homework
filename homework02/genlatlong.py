
#Generate five random pairs of latitudes (between 16.0 - 18.0 degrees North) and longitudes (between 82.0 - 84.0 degrees East) in decimal notation
#For each landing site, also randomly choose a meteorite composition from the list 
#["stony", "iron", "stony-iron"]
#Assemble these data into a dictionary with one key, “sites”, whose value is a list of dictionaries
#Use the Python json library to save the data to a JSON file.

import json
import random
    #https://docs.python.org/3/library/random.html

sites = []
composition = ["stony", "iron", "stony-iron"]
latitude_range = (16.0, 18.0)
longitude_range = (82.0, 84.0)

for i in range(1,6):
    #Uniform specifies a name, random.random does not
    site_id = i;
    #Gernerate random pairs of lats and longs in decimal notation
    lat = random.uniform(latitude_range[0], latitude_range[1])
    lon = random.uniform(longitude_range[0], longitude_range[1])
    #Choose a random meteorite composition
    comp = random.choice(composition)
        #random.choice - Return a rand elem from the non-empty sequence seq.
    sites.append({
        'site_id': site_id, 
        'latitude': lat, 
        'longitude': lon, 
        'composition': comp 
        })

data = {'sites': sites}

#Unit 2 - Working with Common Data Formats, Write to JSON File
with open('meterorite_landings.json', 'w') as out:
    json.dump(data, out, indent = 2)
