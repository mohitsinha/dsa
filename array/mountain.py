# https://leetcode.com/problems/valid-mountain-array/submissions/


def validMountainArray(self, arr):
    if len(arr) < 3:
        return False

    l = 0
    r = len(arr) - 1

    while l <= r:
        if r == 0 or l == len(arr) - 1:
            return False

        if l == r:
            return True

        l_cl = arr[l + 1] > arr[l]
        r_cl = arr[r - 1] > arr[r]

        if l_cl:
            l += 1

        if r_cl:
            r -= 1

        if not l_cl and not r_cl:
            return False

def validMountainArray(self, arr):
    if len(arr) < 3:
        return False

    i = 0
    while i < len(arr) - 1:

        if arr[i + 1] > arr[i]:
            i += 1
        else:
            break

    if i == 0:
        return False

    if i == len(arr) - 1:
        return False

    while i < len(arr) - 1:
        if arr[i + 1] < arr[i]:
            i += 1
        else:
            break

    if i == len(arr) - 1:
        return True
    return False


def validMountainArray(self, arr):
    if len(arr) < 3:
        return False

    i = 0
    j = len(arr) - 1
    while i < len(arr) - 1 and arr[i] < arr[i + 1]:
        i += 1

    while j > 0 and arr[j] < arr[j - 1]:
        j -= 1

    if i > 0 and i == j and j < len(arr) - 1:
        return True
    return False
