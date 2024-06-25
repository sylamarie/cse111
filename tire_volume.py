import math
import datetime 

# show the tire prices for several tire sizes
tire_prices = {
    (185, 65, 15): 100,
    (195, 60, 16): 120,
    (205, 55, 17): 140, 
    (215, 50, 18): 160 
}

# get input from a user 
tire_width = int(input('Enter the width of the tire in mm (ex 205): '))
aspect_ratio = int(input('Enter the aspect ratio of the tire (ex 60): '))
wheel_diameter = int(input('Enter the diameter of the wheel in inches (ex 15): '))

# calculate volume 
tire_volume = math.pi * tire_width**2 * aspect_ratio * (tire_width * aspect_ratio + 2540 * wheel_diameter) / 10000000000

# display result 
print (f'The approximate volume is {tire_volume:.2f} liters')

# check if tire size exists in the price dictionary
if (tire_width, aspect_ratio, wheel_diameter) in tire_prices:
    print('Price for the selected tire size:', tire_prices[(tire_width, aspect_ratio, wheel_diameter)])
elif (tire_width, aspect_ratio, wheel_diameter) == (225, 60, 19):
    print('Price for the selected tire size:', 180)
else:
    print('Tire price not available for the selected size.')

# ask the user if they want to buy tires
buy_tires = input('\nDo you want to buy tires with these dimentions? (yes/no): ').lower()

if buy_tires == 'yes':
    # get user's phone number 
    phone_number = input('Please enter your phone number: ')


    # curent date
    current_date = datetime.date.today()

    with open('volume.txt','a') as f:

        f.write('{}, {}, {}, {}, {}, {}\n'.format(
            current_date,
            tire_width,
            aspect_ratio,
            wheel_diameter,
            round(tire_volume, 2),
            phone_number
        ))
    print('\nThank you! Your phone number has been saved.')
else:
    print('\nThank you for using the tire volume calculator.')