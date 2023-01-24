

Kris Hanks
COE 332 - Spring 2023
Homework 2

Part 1 - getlatlong.py
- Write a Python script to randomly generate latitude, longitude, and compositions for the five meteorite landing sites.
- The latitudes range between 16.0 - 18.0 degrees North 
- The longitudes range between 82.0 - 84.0 degrees East in decimal notation.
- For each landing site, also randomly choose a meteorite composition: stony, iron, stony-iron.
- Use json to save the data to a json file (meterorite_landings.json)

Part 2 - traveltime.py
- Reads in the meteorite site JSON file (meterorite_landings.json) and calculates the time required to visit and take samples from the five sites in order.
- Assume starting position longitude/latitude is {16.0, 82.0}
- Assume the robot visits the site in order listed. 
- Assume radius of Mars is 3389.5 km. 
- Use the great-circle distance algorithm to calculate distance between points.
- Amount of time at each stop depends of composition.
	- Stony = 1hr
	- Iron = 2hr
	- Stony-Iron = 3hr

