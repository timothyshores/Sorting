def selection_sort(arr):
    for i in range(0, len(arr) - 1):
        current_num = arr[i]
        count = 1
        for j in arr[i + 1:]:
            if current_num > j:
                arr[i], arr[i + count] = arr[i + count], arr[i]
            count += 1
    return arr


print("\nSelection Sort")
print(f"[]: {selection_sort([])}")
print(f"[1]: {selection_sort([1])}")
print(f"[1,2]: {selection_sort([1,2])}")
print(f"[2,1]: {selection_sort([2,1])}")
print(f"[1,2,3]: {selection_sort([1,2,3])}")
print(f"[3,2,1]: {selection_sort([3,2,1])}")
print(f"[1,2,3, 4]: {selection_sort([1,2,3,4])}")
print(f"[4,3,2,1]: {selection_sort([4,3,2,1])}\n")


# TO-DO:  implement the Bubble Sort function below


def bubble_sort(arr):

    return arr


# STRETCH: implement the Count Sort function below
def count_sort(arr, maximum=-1):

    return arr
