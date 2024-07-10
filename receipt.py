import csv

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

def main():
    # Read the products.csv file into a dictionary
    filename = 'products.csv'
    key_column_index = 0
    products_dict = read_dictionary(filename, key_column_index)
    
    # Print the products_dict for debugging purposes
    print("All Products")
    print(products_dict)
    
    # Open the request.csv file for reading
    with open('request.csv', mode='r') as file:
        reader = csv.reader(file)
        next(reader)  # Skip the header row
        print("Requested Items")
        for row in reader:
            product_number = row[0]
            quantity = int(row[1])
            
            # Find the corresponding product in products_dict
            product_info = products_dict[product_number]
            product_name = product_info[1]
            product_price = float(product_info[2])
            
            # Print the product name, requested quantity, and product price
            print(f"{product_name}: {quantity} @ {product_price:.2f}")

if __name__ == "__main__":
    main()