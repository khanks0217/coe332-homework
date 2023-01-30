
import math
import json

trip_info = []
speed = 10 #km/hr
radius = 3389.5

#Great-Circle distance algorithm : distance between points
def calc_gcd(latitude_1: float, longitude_1: float, latitude_2: float, longitude_2: float) -> float:
        lat1, lon1, lat2, lon2 = map( math.radians, [latitude_1, longitude_1, latitude_2, longitude_2] )
        d_sigma = math.acos( math.sin(lat1) * math.sin(lat2) + math.cos(lat1) * math.cos(lat2) * math.cos(abs(lon1-lon2)))
        return ( radius * d_sigma )

#print(ml_data['sites'][2]['latitude'])

def travel_time(a_list_of_dicts):
#for i in ml_data['sites']:
    robot_location = (16.0, 82.0)
    totaltime = 0
    totaldist = 0

    #Assume robot visits five sites in order of the list index
    for i in range(len(a_list_of_dicts)):
        latitude = a_list_of_dicts[i]['latitude']
        longitude = a_list_of_dicts[i]['longitude']

        #Great Circle Distance Algorithm - distance between points
        dist = calc_gcd(robot_location[0], robot_location[1], latitude, longitude)
        totaldist = totaldist + dist
        traveltime = dist/speed
        totaltime = totaltime + traveltime
        #Update robot_location
        robot_location = (latitude, longitude);
        #Update sampletime
        if ml_data['sites'][i]['composition'] == 'stony':
            sampletime = '1 hr'
        elif ml_data['sites'][i]['composition'] == 'iron':
            sampletime = '2 hr'
        elif ml_data['sites'][i]['composition'] == 'stony-iron':
            sampletime = '3 hr'
        else:
            sampletime = 'help'
    
        trip_info.append({'leg': ml_data['sites'][i]['site_id'],
                'time to travel': traveltime,
                'time to sample': sampletime
                })
        print(trip_info[i], sep = '\n')
    #Trip is "over" after sampling last meteorite
    #Print descriptive summary info:
    print("Total Travel Time = " , totaltime , "hr")
    print("Total Travel Distance = " , totaldist , "km")
    return(trip_info)

#Use json library to read in data from meterorite_landings.json
with open('meterorite_landings.json', 'r') as f:
    ml_data = json.load(f)

travel_time(ml_data['sites'])
