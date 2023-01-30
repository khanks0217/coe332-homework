

Kris Hanks

COE 332 - Spring 2023

Homework 2

**Part 1 - genlatlong.py**

The python script, genlatlong.py, randomly generates latitude, longitude, and compositions for five meteorite landing sites. The latitudes ranges between 16.0 - 18.0 degrees North; the longitudes ranges between 82.0 - 84.0 degrees East in decimal notation. At each landing site, a random meteorite composition is chosen: stony, iron, stony-iron. Once the script is run, the data is updated in the json file (meterorite_landings.json).

**Part 2 - traveltime.py**

The python script genlatlong.py reads in the meteorite site JSON file (meterorite_landings.json) and calculates the time required to visit and take samples from the five sites in order.Script assumes: starting position longitude/latitude is {16.0, 82.0}, radius of Mars is 3389.5 km. Use the great-circle distance algorithm to calculate distance between points. The amount of time at each stop depends of composition {Stony = 1hr, Iron = 2hr, Stony-Iron = 3hr"

**Running the Code**

This code has two functions:

	- Generate random latitude, longitude, and compositions of meteorite landings.

	- Calculate distance, travel time, and time to sample between landings.

To run genlatlong.py 

	'python3 genlatlong.py'

	'#Returns data in meterorite_landings.json'

	'python3 traveltime.py'

**Usage**

'import json'

'import random'

'import math'

**Expected Output, Sample**

{'leg': 1, 'time to travel': 10.270618530606296, 'time to sample': '1 hr'}

{'leg': 2, 'time to travel': 0.43565369913125523, 'time to sample': '3 hr'}

{'leg': 3, 'time to travel': 2.056478097733949, 'time to sample': '1 hr'}

{'leg': 4, 'time to travel': 10.280838081669298, 'time to sample': '3 hr'}

{'leg': 5, 'time to travel': 8.46528382921807, 'time to sample': '2 hr'}

Total Travel Time =  31.508872238358865 hr
Total Travel Distance =  315.0887223835887 km
