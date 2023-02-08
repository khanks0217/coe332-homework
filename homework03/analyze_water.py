import json
import requests
import math
from typing import List

def water_turbidity(CalibConstData:List[float], DetectorCurrentData:List[float]) -> float:
    """
    The function water_turbidity calculates the current water turbidity
    by taking the average of the five most recent data points.

    Arguments:
    data -- a list of float values containing water quality

    Returns:
    float -- the average turbidity of the 5 data points
    """

    # T - Turbidity in NTU Units (0 - 40)
    # a0 - Calibration Constant
    # I90 - Ninety degree detector current
    T = 0
    for i in range(-5,0):
        T = T + (CalibConstData[i] * DetectorCurrentData[i])
    T = T/5
    return T

def threshold(T : float) -> float:
    """
    The function threshold calculate the minimum time for the water turbidity to 
    fall below the safe threshiold.

    Arguments:
    T -- a float representing the current water Turbidity

    Returns:
    float -- the minimum time required for the water turbidity to fall below 
    the threshold
    """
    Ts = 1.0 #Turbidity threshold for safe water
    d= 0.02 #Decay factor per hour

    if T <= Ts:
        return 0.0 #If water is already safe
    else:
        return (math.log(Ts/T) / (math.log(1-d)))

def main():
    response = requests.get("https://raw.githubusercontent.com/wjallen/turbidity/main/turbidity_data.json")
    water_data = json.loads(response.text)

    #Collect calibration constant and detector current values.
    calib_const = [item['calibration_constant'] for item in water_data['turbidity_data']]
    detector_curr = [item['detector_current'] for item in water_data['turbidity_data']]

    #Calculate water turbidity. 
    turb = water_turbidity(calib_const, detector_curr)
    print("\nAverage turbidity based on most recent five measurements: ", turb, "NTU");

    #Check water turbidity levels.
    if turb > 1.0:
        print("Warning: Turbidity is above threshold for safe use.")
    else:
        print("Info: Turbidity is within threshold for safe use.")

    #Calculate time until within threshold
    print("Time until below threshold: ", threshold(turb), "hrs.\n")

if __name__ == '__main__':
    main()
