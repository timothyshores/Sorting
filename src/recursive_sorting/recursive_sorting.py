# TO-DO: complete the helpe function below to merge 2 sorted arrays
def merge(arrA, arrB):
    merged_arr = []  # initialize an empty list to return
    elements = len(arrA) + len(arrB)  # sum of elements in arrA and arrB
    if len(arrA) == 0 and len(arrB) > 0:  # if arrA is [] then return arrB
        merged_arr = arrB
    elif len(arrA) > 0 and len(arrB) == 0:  # if arrB is [] then return arrA
        merged_arr = arrA
    else:  # if arrA and arrB are both non-empty arrays
        while elements > 0:
            if len(arrA) > 0:
                # creates a pointer to the first element in arrA if arrA != []
                a_pointer = arrA[0]
            else:
                merged_arr.extend(arrB)
                break
            if len(arrB) > 0:
                # creates a pointer to the first element in arrB if arrB != []
                b_pointer = arrB[0]
            else:
                merged_arr.extend(arrA)
                break
            if a_pointer <= b_pointer:  # array A cointains a smaller first value then array B
                # add the first element in array A to the end of merged_arr
                merged_arr.append(a_pointer)
                # remove the first element in array A
                del arrA[0]
            else:  # array A cointains a smaller first value then array B
                # add the first element in array B to the end of merged_arr
                merged_arr.append(b_pointer)
                # remove the first element in array A
                del arrB[0]
            elements = len(arrA) + len(arrB)
    return merged_arr

# TO-DO: implement the Merge Sort function below USING RECURSION


def merge_sort(arr):
    # TO-DO

    return arr


# STRETCH: implement an in-place merge sort algorithm
def merge_in_place(arr, start, mid, end):
    # TO-DO

    return arr


def merge_sort_in_place(arr, l, r):
    # TO-DO

    return arr


# STRETCH: implement the Timsort function below
# hint: check out https://github.com/python/cpython/blob/master/Objects/listsort.txt
def timsort(arr):

    return arr
