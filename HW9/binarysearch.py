# binary search
def binary_search(arr, target):
    l = 0
    h = len(arr) - 1
    count = 0
    while l <= h:
        mid = (h + l) // 2
        count += 1

        if arr[mid] == target:
            return mid, count
        elif arr[mid] < target:
            l = mid + 1
        else:
            h = mid - 1

    return -1, count


arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
index, step = binary_search(arr, 3)
print(binary_search(arr, 4))
print(f"index : {index} step: {step}")
