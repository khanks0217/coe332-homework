Kris Hanks

COE 332 - Spring 2023

Homework 4

**Data Collected From:**
https://nasa-public-data.s3.amazonaws.com/iss-coords/current/ISS_OEM/ISS.OEM_J2K_EPH.xml

**iss_TRACKER.py**

The python script, iss_TRACKER.py, reads in the ‘Orbital Ephemeris Message (OEM)’ data in XML format which contains ISS state vectors over an ~15 day period.‘State vectors’ are the Cartesian vectors for both position {X, Y, Z} and velocity {X_DOT, Y_DOT, Z_DOT} that, along with a time stamp (EPOCH), describe the complete state of the system (the ISS).

Flask Application Routes:

	Route: "/" - Returns the entire data set.
	
	Route: "/epochs" - Returns a list of all Epochs in the data set. 

	Route: "/epochs/<epoch>" - Returns a state vector for specified epoch. 

	Route: "/epochs/<epoch>/speed" - Returns instantaneous speed for specified epoch. 


**Running iss_TRACKER.py**

	On one terminal window, start the Flask app.

		flask --app iss_TRACKER --debug run --port 5000

	In a different terminal window, run the different routes by following the respective commands. 

		curl localhost:5000/

		curl localhost:5000/epoch

		curl localhost:5000/epoch/2023-059T10:49:00.000Z	

		curl localhost:5000/epoch/2023-059T10:49:00.000Z/speed

**Expected Output, Sample**

	Sample Output for curl localhost:5000/
		{
  			"OEM": [
    				{
      				"EPOCH": "2023-044T12:00:00.000Z",
      				"x": "-4521.4974282552303",
      				"x_dot": "-4.1589478421027897",
      				"y": "1255.8970985543799",
      				"y_dot": "-6.0017229173095901",
      				"z": "-4915.6447650913897",
      				"z_dot": "2.3010458138354202"
    				}, (continued)		
	
	Sample Output for curl localhost:5000/epochs
			{
  				"epochs": [
   					"2023-044T12:00:00.000Z",
    					"2023-044T12:04:00.000Z",
    					"2023-044T12:08:00.000Z",
    					"2023-044T12:12:00.000Z",
    					"2023-044T12:16:00.000Z",
    					"2023-044T12:20:00.000Z",
    					"2023-044T12:24:00.000Z",
					(continued)

	Sample Output for curl localhost:5000/epochs/2023-059T10:49:00.000Z
		{
		  "state_vectors": {
		    "x": "-1661.0466270982599",
		    "x_dot": "6.64886336653813",
		    "y": "-3912.91371833423",
		    "y_dot": "-3.7518916669779698",
		    "z": "5291.9541026185498",
		    "z_dot": "-0.67811312275952995"
  		}
		}

	Sample Output for curl localhost:5000/epoch/2023-059T10:49:00.000Z/speed
		{
		  "speed": 7.664457746957065
		}
