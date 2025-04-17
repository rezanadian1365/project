# binary search
def binary_search(arr, target):
    l = 0
    h = len(arr) - 1
    while l <= h:
        mid = (l - h) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            l = mid + 1
        else:
            h = mid - 1
    return -1


arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
binary_search(arr, 3)
print(binary_search(arr, 3))
