def water_column_height(tower_height, tank_height):
    water_height = tower_height + (3 * tank_height) / 4
    return water_height 

def pressure_gain_from_water_height(height):
    density_water = 998.2 # kg/m^3
    gravity = 9.80665 # m/s^2
    kilopascals_pressure = (density_water * gravity * height) / 1000
    return kilopascals_pressure

def pressure_loss_from_pipe(pipe_diameter,
        pipe_length, friction_factor, fluid_velocity):
    density_water = 998.2 # kg/m^3
    pressure_lost = (-friction_factor * pipe_length * density_water * fluid_velocity**2) / 2000 * pipe_diameter
    return pressure_lost