from pytest import approx
import pytest
from water_flow import (
    water_column_height,
    pressure_gain_from_water_height,
    pressure_loss_from_pipe,
    pressure_loss_from_fittings,
    reynolds_number,
    pressure_loss_from_pipe_reduction
)
from water_flow import kpa_to_psi

def test_water_column_height():
    test_cases1 = [
    (0.0, 0.0, 0.0),
    (0.0, 10.0, 7.5),
    (25.0, 0.0, 25.0),
    (48.3, 12.8, 57.9)
    ]

    for tower_height, tank_height, expected in test_cases1:
         result = water_column_height(tower_height, tank_height)
         assert result == approx(expected, rel=1e-2)

def test_pressure_gain_from_water_height():
    test_cases2 = [
        (0.0, 0.000, 0.001),
        (30.2, 295.628, 0.001),
        (50.0, 489.450, 0.001)
    ]

    for height, expected, tolerance in test_cases2:
         result = pressure_gain_from_water_height(height)
         assert result == approx(expected, rel=tolerance)

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

    for pipe_diameter, pipe_length, friction_factor, fluid_velocity, expected, tolerance in test_cases3:
         result = pressure_loss_from_pipe(pipe_diameter, pipe_length, friction_factor, fluid_velocity)
         assert result == approx(expected, rel=tolerance)

def test_pressure_loss_from_fittings():
    test_cases4 = [
        (0.00, 3, 0.000, 0.001),
        (1.65, 0, 0.000, 0.001),
        (1.65, 2, -0.109, 0.003),
        (1.75, 2, -0.122, 0.003),
        (1.75, 5, -0.306, 0.001)
    ]

    for fluid_velocity, quantity_fittings, expected, tolerance in test_cases4:
         result = pressure_loss_from_fittings(fluid_velocity, quantity_fittings)
         assert result == approx(expected, rel=tolerance, abs=2.2e-04)
         
def test_reynolds_number():
    test_cases5 = [
        (0.048692, 0.00, 0, 1),
        (0.048692, 1.65, 80069, 1),
        (0.048692, 1.75, 84922, 1),
        (0.286870, 1.65, 471729, 1),
        (0.286870, 1.75, 500318, 1)
    ]

    for hydraulic_diameter, fluid_velocity, expected, tolerance in test_cases5:
         result = reynolds_number(hydraulic_diameter, fluid_velocity)
         assert result == approx(expected, rel=tolerance)

def test_pressure_loss_from_pipe_reduction():
    test_cases6 = [
        (0.28687, 0.00, 1, 0.048692, 0.000, 0.001),
        (0.28687, 1.65, 471729, 0.048692, -163.744, 0.001),
        (0.28687, 1.75, 500318, 0.048692, -184.182, 0.001)
    ]

    for larger_diameter, fluid_velocity, reynolds_number, smaller_diameter, expected, tolerance in test_cases6:
         result = pressure_loss_from_pipe_reduction(larger_diameter, fluid_velocity, reynolds_number, smaller_diameter)
         assert result == approx(expected, rel=tolerance)

def test_kpa_to_psi_conversion():
    test_cases = [
        (0.0, 0.0),
        (100.0, 14.503773773),
        (200.0, 29.007547546),
        (500.0, 72.518868865),
        (1000.0, 145.03773773),
        (1500.0, 217.55660659)
        # Add more test cases as needed
    ]

    for kpa, expected_psi in test_cases:
        result_psi = kpa_to_psi(kpa)
        assert result_psi == approx(expected_psi, rel=1e-6)

# Call the main function that is part of pytest so that the
# computer will execute the test functions in this file.
pytest.main(["-v", "--tb=line", "-rN", __file__])