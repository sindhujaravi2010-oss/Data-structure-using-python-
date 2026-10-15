def linear(a, x):
    for value in a:
        if value == x:
            return True
    return False


def binary(a, x):
    left = 0
    right = len(a) - 1

    while left <= right:
        mid = (left + right) // 2

        if a[mid] == x:
            return True
        elif x > a[mid]:
            left = mid + 1
        else:
            right = mid - 1

    return False
