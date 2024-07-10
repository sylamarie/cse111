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
            value = row[:key_column_index] + row[key_column_index + 1:]
            dictionary[key] = value
    return dictionary

def validate_i_number(i_number):
    """Validate the I-Number.
    Parameters:
        i_number: the I-Number to validate.
    Return: a tuple containing a boolean indicating
        validity and a message string.
    """
    i_number = i_number.replace("-", "")
    
    if not i_number.isdigit():
        return False, "Invalid I-Number"
    if len(i_number) < 9:
        return False, "Invalid I-Number: too few digits"
    if len(i_number) > 9:
        return False, "Invalid I-Number: too many digits"
    
    return True, i_number

def main():
    filename = 'students.csv'
    key_column_index = 0  # Assuming the I-Numbers are in the first column
    students_dict = read_dictionary(filename, key_column_index)
    
    i_number = input("Please enter an I-Number (with or without dashes): ")
    is_valid, result = validate_i_number(i_number)
    
    if not is_valid:
        print(result)
        return
    
    if result in students_dict:
        name = students_dict[result]
        print("Name:", " ".join(name))
    else:
        print("No such student")

if __name__ == "__main__":
    main()