import csv
from datetime import datetime
import random

def read_dictionary(filename, key_column_index):
    """Read the contents of a CSV file into a compound
    dictionary and return the dictionary.
    Parameters
        filename: the name of the CSV file to read.
        key_column_index: the index of the column
            to use as the keys in the dictionary.
    Return: a compound dictionary that contains
        the contents of the CSV file.
    """
    dictionary = {}
    with open(filename, mode='r') as file:
        reader = csv.reader(file)
        next(reader)  # Skip the header row
        for row in reader:
            key = row[key_column_index]
            dictionary[key] = row
    return dictionary

def apply_discounts(original_subtotal, current_datetime):
    # Apply discounts based on the current day and time.
    discount_rate = 0.10  # 10% discount

    # Apply discount if today is Tuesday or Wednesday
    if current_datetime.strftime('%A') in ['Tuesday', 'Wednesday']:
        original_subtotal *= (1 - discount_rate)
    
    # Apply discount if the current time is before 11:00 a.m.
    if current_datetime.hour < 11:
        original_subtotal *= (1 - discount_rate)
    
    return original_subtotal

# Function to generate a random coupon for a product ordered
def generate_coupon(ordered_items):
    """Generate a coupon for a product ordered."""
    if ordered_items:
        random_item = random.choice(ordered_items)
        return random_item[0], float(random_item[2]) * 0.75  # 25% discount on coupon
    else:
        return None, None

def main():
    try:
        # Read the products.csv file into a dictionary
        filename = 'products.csv'
        key_column_index = 0
        products_dict = read_dictionary(filename, key_column_index)

        # Open the request.csv file for reading
        with open('request.csv', mode='r') as file:
            reader = csv.reader(file)
            next(reader)  # Skip the header row
            
            # Print the number of ordered items 
            # and subtotal due.
            total_items = 0
            subtotal = 0.0

            # Print the list of ordered items.
            ordered_items = []

            for row in reader:
                product_number = row[0]
                quantity = int(row[1])

                # Find the corresponding product in products_dict
                product_info = products_dict[product_number]
                product_name = product_info[1]
                product_price = float(product_info[2])

                # Calculate the total price for items
                total_price = quantity * product_price

                # totals
                total_items += quantity
                subtotal += total_price

                # List the ordered item(s)
                ordered_items.append((product_name, quantity, product_price))
            
            # Compute and print the sales tax amount. Use 6% as the sales tax rate.
            sales_tax_rate = 0.06
            sales_tax = subtotal * sales_tax_rate
            total_due = subtotal + sales_tax

            # Current date and time
            current_date_and_time = datetime.now()
            
            # Print the receipt
            print("Store Name: Syla Marie")
            print()
            print('Ordered Items: ')
            for item in ordered_items:
                print(f'{item[0]}: {item[1]} @ ${item[2]:.2f}')
            print()
            print(f'Number of ordered items: {total_items}')
            print(f'Subtotal: ${subtotal:.2f}')
            print(f'Sales Tax: ${sales_tax:.2f}')
            print(f'Total: ${total_due:.2f}')
            print()
            print('Thank you for shopping at the Syla Marie.')
            print(f'Date: {current_date_and_time:%A, %B %d, %H:%M:%S, %Y}')

            # Print coupon for a randomly selected product ordered
            coupon_product, coupon_price = generate_coupon(ordered_items)
            if coupon_product:
                print()
                print("Coupon for your next purchase:")
                print(f"Get 25% off {coupon_product}! Now ${coupon_price:.2f} each.")

            # Print invitation for an online survey
            print()
            print("Please visit our website to complete a quick survey about your shopping experience.")

    except FileNotFoundError:
        print("Error: missing file")
        print(e)
    except PermissionError as e:
        print(f"Error: Permission denied for file {e.filename}.")
    except KeyError as e:
        print("Error: unknown product ID in the request.csv file")
        print(e)

if __name__ == "__main__":
    main()