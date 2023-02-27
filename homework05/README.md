# **Containerized ISS Tracker**

Kris Hanks

Homework05, COE332 - Spring 2023

**Project Objective**
Sift through an abundance of positional and velocity data for the International Space Station (ISS). Build
 a Flask application for querying and returning information from the ISS data set. The included Dockerfile
 containerizes iss_tracker.py to make it portable.

**Data Collected From:**
https://nasa-public-data.s3.amazonaws.com/iss-coords/current/ISS_OEM/ISS.OEM_J2K_EPH.xml

**ISS Data Description**
I STILL NEED TO WRITE A DESCRIPTION

**iss_tracker.py Description:**

The python script, iss_TRACKER.py, reads in the ‘Orbital Ephemeris Message (OEM)’ data in XML format which
 contains ISS state vectors over an ~15 day period.‘State vectors’ are the Cartesian vectors for both posi
tion {X, Y, Z} and velocity {X_DOT, Y_DOT, Z_DOT} that, along with a time stamp (EPOCH), describe the comp
lete state of the system (the ISS).

**Dockerfile Description & Instructions**

How to pull and use the Dockerfule from Docker Hub:
	I STILL NEED TO DO THIS

How to build a new image from Dockerfile:

	docker build -t username/iss_tracker:1.1 .

Test newly built image:

	docker run -it --rm -p 5000:5000 khanks/iss_tracker:1.1

With the iss_tracker container running, curl in another window to interact with the program.

**Flask API Front End:**

The API front end is expose on port 5000 inside the container. Try the following routes:


	$ curl localhost:5000/

	/ 				Returns the entire data set.
	
	/epochs				Returns a list of all Epochs in the data set. 

	/epochs?limit=int&offset=int" 	Returns modified list of Epochs given query parameters. 

	/epochs/<epoch> 		Returns a state vector for specified epoch. 

	/epochs/<epoch>/speed		Returns instantaneous speed for specified epoch. 

	/help 				Returns help text (as a string) that briefly describes each route.

	/delete-data 			Delete all data from the dictionary object.

	/post-data			Reload the dictionary object with data from the web.


**Running iss_tracker.py**

On one terminal window, build and run the docker.
	
		docker build -t khanks/iss_tracker:1.1 .

		docker run -it --rm -p 5000:5000 khanks/iss_tracker:1.1
	
Exit the iss_tracker container to run the flask applicaiton. 
		
		flask --app iss_tracker --debug run --port 5000
	
In a different terminal window, run the different routes by following the respective commands. 

		curl localhost:5000/

		curl localhost:5000/epochs

		curl localhost:5000/epochs?limit=20&offset=50

		curl localhost:5000/epochs/2023-059T10:49:00.000Z	

		curl localhost:5000/epochs/2023-059T10:49:00.000Z/speed

		curl -X DELETE localhost:5000/delete-data
	
		curl -X POST localhost:5000/post-data
	
**Expected Output, Sample**

Sample Output for docker build -t khanks/iss_tracker:1.1 .                                    

                Sending build context to Docker daemon  3.062MB                                       
                Step 1/6 : FROM python:3.8.10                                                         
                 ---> a369814a9797                                                                    
                Step 2/6 : RUN pip install requests==2.26.0                                           
                 ---> Using cache                                                                     
                 ---> 3d7d5d3d3c53                                                                    
                Step 3/6 : RUN pip install Flask==2.2.2                                               
                 ---> Using cache                                                                     
                 ---> 2d89d63bf54e                                                                    
                Step 4/6 : RUN pip install xmltodict==0.12.0                                          
                 ---> Running in cb729db53967
                Collecting xmltodict==0.12.0
                  Downloading xmltodict-0.12.0-py2.py3-none-any.whl (9.2 kB)                          
                Installing collected packages: xmltodict                                              
                Successfully installed xmltodict-0.12.0                                               
                Removing intermediate container cb729db53967                                          
                 ---> 524cdc9bc824                                                                    
                Step 5/6 : COPY iss_tracker.py /iss_tracker.py
                 ---> 70a150e108c4
                Step 6/6 : CMD ["python", "iss_tracker.py"]                                           
                 ---> Running in e1622a419a3e                                                         
                Removing intermediate container e1622a419a3e                                          
                 ---> d8ffe49eea2a                                                                    
                Successfully built d8ffe49eea2a                                                       
                Successfully tagged khanks/iss_tracker:1.1

Sample Output for docker run -it --rm -p 5000:5000 khanks/iss_tracker:1.1                     

                * Serving Flask app 'iss_tracker'                                                     
                * Debug mode: on                                                                      
                WARNING: This is a development server. Do not use it in a production deployment. Use a production WSGI server instead.
                 * Running on all addresses (0.0.0.0)                                                 
                 * Running on http://127.0.0.1:5000                                                   
                 * Running on http://172.17.0.2:5000                                                  
                Press CTRL+C to quit                                                                  
                 * Restarting with stat
                 * Debugger is active!                                                                
                 * Debugger PIN: 493-291-309                                                          
                172.17.0.1 - - [25/Feb/2023 19:23:49] "GET /degrees HTTP/1.1" 404 - 

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

Sample Output for curl localhost:5000/epochs?limit20&offset=50

		"epochs": [
			    "2023-053T12:00:00.000Z",
			    "2023-053T12:04:00.000Z",
			    "2023-053T12:08:00.000Z",
			    "2023-053T12:12:00.000Z",
			    "2023-053T12:16:00.000Z",
			    "2023-053T12:20:00.000Z",
			    "2023-053T12:24:00.000Z",
			    "2023-053T12:28:00.000Z",
			    "2023-053T12:32:00.000Z",
			    "2023-053T12:36:00.000Z",
			    "2023-053T12:40:00.000Z",
			    "2023-053T12:44:00.000Z",
			    "2023-053T12:48:00.000Z",
			    "2023-053T12:52:00.000Z",
			    "2023-053T12:56:00.000Z",
			    "2023-053T13:00:00.000Z",
			    "2023-053T13:04:00.000Z",
			    "2023-053T13:08:00.000Z",
			    "2023-053T13:12:00.000Z",
			    "2023-053T13:16:00.000Z"
		  ]
		}	

Sample Output for curl localhost:5000/epochs/2023-053T13:08:00.000Z

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

Sample Output for curl localhost:5000/epoch/2023-053T13:08:00.000Z/speed

		{
		  "speed": 7.664457746957065
		}

Sample Output for curl -X DELETE localhost:5000/delete-data                                   

                All data deleted successfully.                                                        
                                                                                                      
                After deleting, curl localhost:5000/epochs return                                     
                {                                                                                     
                  "epochs": []                                                                        
                }

Sample Output for curl -X POST localhost:5000/post-data

		Data restored. 
