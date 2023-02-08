from analyze_water import water_turbidity, threshold
import pytest

def test_water_turbidity():
    """
    Simple test function to verify test_water_turbidity is working properly. 
    
    Arguments - NONE

    Returns - Assertion error if working imporperly.
    """

    calib_const = [1.0, 1.0, 1.0, 1.0, 1.0]
    det_curr = [1.0, 1.0, 1.0, 1.0, 1.0]
    expected_value = 1.0
    assert water_turbidity(calib_const, det_curr) == expected_value

def test_threshold():
    """
    Simple test function to verify that the threshold function is working properly.

    Arguments - NONE

    Returns - Assertion error if working improperly.
    """
    testT = 1.0
    expected_value = 0.0
    assert threshold(testT) == expected_value

