from random import randint


def add_arrays(first_array, second_array):
    result_array = []
    carry = 0
    for i in range(9, -1, -1):
        total = first_array[i] + second_array[i] + carry
        carry = total // 10
        result_array.insert(0, total % 10)
    if carry > 0:
        result_array.insert(0, carry)
    return result_array


def subtract_arrays(first_array, second_array):
    result_array = []
    borrow = 0
    for i in range(9, -1, -1):
        diff = first_array[i] - second_array[i] - borrow
        if diff < 0:
            diff += 10
            borrow = 1
        else:
            borrow = 0
        result_array.insert(0, diff)
    return result_array


operation = input("Choose operation (+ or -): ")

first_array = []
second_array = []

for i in range(10):
    first_array.append(randint(0, 9))
    second_array.append(randint(0, 9))

print(f"First array: {first_array}")
print(f"Second array: {second_array}")

if operation == '+':
    result_array = add_arrays(first_array, second_array)
    print(f"result (+): {result_array}")
elif operation == '-':
    result_array = subtract_arrays(first_array, second_array)
    print(f"Result (-): {result_array}")
else:
    print("Wrong operation. Please, choose + or -.")

