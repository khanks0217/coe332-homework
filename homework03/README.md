Kris Hanks

COE 332 - Spring 2023

Homework 3

**Data Collected From:**
https://raw.githubusercontent.com/wjallen/turbidity/main/turbidity_data.json

**Part 1 - analyze_water.py**

The python script, analysze_water.py, reads in the water quality data set and prints key pieces of information:
	1. The current water turbidity taken as an average of the 5 most recent data points.
		Equation: Turbidity = Calibration Constant * Ninety Degree Detector Current
	2. Whether the calculated turbididty is below a safe threshold. 
	3. The minimum time required for turbidity to be within a safe threshold. 

**Part 2 - test_analyze_water.py**

The python script, test_analyze_water.py, is a unit test script to test the functions in analyze_water.py. There is at least one test associated with each function which perform simple mathematical sanity checks.  

**Running the Code**

To run genlatlong.py

        'python3 analyze_water.py'

        'python3 test_analyze_water.py'

**Usage**

'import json'

'import requests'

'import pytest'

**Expected Output, Sample**

Average turbidity based on most recent five measurements = 1.1992 NTU

Warning: Turbidity is above threshold for safe use

Minimum time required to return below a safe threshold = 8.99 hours

