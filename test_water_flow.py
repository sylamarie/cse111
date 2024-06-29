from pytest import approx
import pytest
from water_flow import water_column_height

def test_water_column_height():
    test_cases1 = [
    (0.0, 0.0, 0.0),
    (0.0, 10.0, 7.5),
    (25.0, 0.0, 25.0),
    (48.3, 12.8, 57.9)
    ]

def test_pressure_gain_from_water_height():
    test_cases2 = [
        (0.0, 0.000, 0.001),
        (30.2, 295.628, 0.001),
        (50.0, 489.450, 0.001)
    ]

def  test_pressure_loss_from_pipe():
    test_cases3 = [
        (0.048692, 0.00, 0.018, 1.75, 0.000, 0.001),
        (0.048692, 200.00, 0.000, 1.75, 0.000, 0.001),
        (0.048692, 200.00, 0.018, 0.00, 0.000, 0.001),
        (0.048692, 200.00, 0.018, 1.75, -113.008, 0.001),
        (0.048692, 200.00, 0.018, 1.65, -100.462, 0.001),
        (0.286870, 1000.00, 0.013, 1.65, -61.576, 0.001),
        (0.286870, 1800.75, 0.013, 1.65, -110.884, 0.001)
    ]

# Call the main function that is part of pytest so that the
# computer will execute the test functions in this file.
pytest.main(["-v", "--tb=line", "-rN", __file__])