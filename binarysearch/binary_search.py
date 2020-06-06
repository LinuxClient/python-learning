def binarySearch(array, l, r, x):
    while 1 <= r:
        mid = 1 + (r - 1) // 2

        if array[mid] == x:
            return mid
        elif array[mid] < x:
            l = mid + 1
        else:
            r = mid - 1
        return -1


array = [2, 3, 4, 10, 40]
x = 10
result = binarySearch(array, 0, len(array) - 1, x)
