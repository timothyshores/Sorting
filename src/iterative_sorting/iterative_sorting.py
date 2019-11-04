def selection_sort(arr):
    for i in range(0, len(arr) - 1):
        current_num = arr[i]
        count = 1
        for j in arr[i + 1:]:
            if current_num > j:
                arr[i], arr[i + count] = arr[i + count], arr[i]
            count += 1
    return arr

# TO-DO:  implement the Bubble Sort function below


def bubble_sort(arr):
    print(f"\nInput array: {arr}\n")
    index = 0
    iteration = 0
    for i in arr[:-1]:
        print(f"Iteration: {index + 1}\n__________________")
        for j in arr[index + 1:]:
            print(f"i: {i}, j: {j}, index: {index}, iteration: {iteration}")
            print(f"Current array: {arr}")
            if i > j:
                print(f"Before swap: {arr}")
                print((" " * 3 * index) + (" " * 14) + "^")
                arr[index], arr[index + 1] = arr[index + 1], arr[index]
                print(f"After swap: {arr}")
                print((" " * 3 * index) + (" " * 16) + "^\n")
            index += 1
        iteration += 1
        index = iteration
        print()
    print()
    if min(arr) != arr[0]:
        print(f"Min: {min(arr)}, arr[0]: {arr[0]}")
        bubble_sort(arr)
    return arr

# STRETCH: implement the Count Sort function below


def count_sort(arr, maximum=-1):

    return arr
