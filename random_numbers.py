import random

def main():
    numbers = [16.2, 75.1, 52.3]

    print('numbers')
    print(numbers)

    append_random_numbers(numbers, 1)
    print('numbers')
    print(numbers)

    append_random_numbers(numbers, 3)
    print('numbers')
    print(numbers)

def append_random_numbers(number_list, quantity = 1):
     for _ in range(quantity):
        random_number = round(random.uniform(0, 100), 1)
        number_list.append(random_number)

if __name__ == "__main__":
    main()