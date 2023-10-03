from random import randint


def fill_array_with_random_numbers(arr, size):
    for i in range(size):
        arr.append(randint(1, 9))


def add_arrays_with_carry(first_array, second_array):
    temp = 0
    max_size = max(len(first_array), len(second_array))

    while len(first_array) < len(second_array):
        first_array.insert(0, 0)
    while len(second_array) < len(first_array):
        second_array.insert(0, 0)

    for i in range(max_size - 1, -1, -1):
        first_digit = first_array[i] if i < len(first_array) else 0
        second_digit = second_array[i] if i < len(second_array) else 0
        total = first_digit + second_digit + temp
        temp = total // 10
        result_array.insert(0, total % 10)

    if temp > 0:
        result_array.insert(0, temp)

    return result_array


def subtract_arrays_with_borrow(first_array, second_array):
    temp = 0
    max_size = max(len(first_array), len(second_array))

    while len(first_array) < len(second_array):
        first_array.insert(0, 0)
    while len(second_array) < len(first_array):
        second_array.insert(0, 0)

    for i in range(max_size - 1, -1, -1):
        first_digit = first_array[i] if i < len(first_array) else 0
        second_digit = second_array[i] if i < len(second_array) else 0
        total = first_digit - second_digit - temp

        if total < 0:
            total += 10
            temp = 1
        else:
            temp = 0

        result_array.insert(0, total)

    # Remove leading zeros
    while len(result_array) > 1 and result_array[0] == 0:
        result_array.pop(0)

    return result_array


first_array = []
second_array = []
result_array = []

first_arr_size = int(input("Enter size of 1 arr: "))
second_arr_size = int(input("Enter size of 2 arr: "))

fill_array_with_random_numbers(first_array, first_arr_size)
fill_array_with_random_numbers(second_array, second_arr_size)

operation_choice = input("Enter 'add' for addition or 'subtract' for subtraction: ")

if operation_choice.lower() == 'add':
    add_arrays_with_carry(first_array, second_array)
elif operation_choice.lower() == 'subtract':
    subtract_arrays_with_borrow(first_array, second_array)
else:
    print("Invalid choice. Please enter 'add' or 'subtract'.")


print(f"First array: {first_array}")
print(f"Second array: {second_array}")
print(f"Addition Result: {result_array}")
