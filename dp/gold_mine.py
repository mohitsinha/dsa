mat = [
    [10, 33, 13, 15],
    [22, 21, 4, 1],
    [5, 0, 2, 3],
    [0, 6, 14, 2]]

length = len(mat[0])

a = [0 for i in range(length)]


def mine(i, j):
    right = 0
    right_top = 0
    right_bottom = 0

    # calculate just right
    if j + 1 < len(mat[0]):
        right = mine(i, j + 1)

    # calculate just right-top
    if j + 1 < len(mat[0]) and i - 1 >= 0:
        right_top = mine(i - 1, j + 1)

    # calculate just right-bottom
    if j + 1 < len(mat[0]) and i + 1 < len(mat):
        right_bottom = mine(i + 1, j + 1)

    maximum = mat[i][j] + max(right, right_top, right_bottom)
    return maximum


maximum = 0
for i in range(len(mat)):
    val = mine(i, 0)
    maximum = max(val, maximum)

print(maximum)
# for i in range(length):
#     mat[i]=max( )

arr = [[0 for i in range(len(mat[0]))] for i in range(len(mat))]
for j in range(len(mat[0])):

    for i in range(len(mat)):
        val = mat[i][j]
        left = 0
        leftBottom = 0
        leftTop = 0
        # left
        if  j - 1 >= 0:
            left = arr[i ][j - 1]
        # leftBottom
        if i + 1 < len(mat) and j - 1 >= 0:
            leftBottom = arr[i + 1][j - 1]
        # leftTop
        if i - 1 >= 0 and j - 1 >= 0:
            leftTop = arr[i - 1][j - 1]
        arr[i][j] = val + max(left, leftTop, leftBottom)

print(arr)

import operator as op
from functools import reduce


def ncr(n, r):
    r = min(r, n-r)
    numer = reduce(op.mul, range(n, n-r, -1), 1)
    denom = reduce(op.mul, range(1, r+1), 1)
    return numer / denom

v= ncr(3,0)+ncr(3,1)+ncr(3,2)+ncr(3,3)
print(v)
