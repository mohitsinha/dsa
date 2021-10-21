# https://leetcode.com/problems/jump-game/submissions/

def canJump(self, arr) -> bool:
    n = len(arr)
    if n == 1:
        return True
    if arr[0] == 0:
        return False
    if n == 2:
        return True

    z = False

    i = n - 2
    while i >= 0:

        if arr[i] == 0:
            z = True
            ind = i
            i -= 1
            while i >= 0:
                if arr[i] > ind - i:
                    z = False
                    break
                else:
                    i -= 1

        i -= 1

    print(z)
    return (not z) or False

def canJump1(self, arr) -> bool:

    n = len(arr)

    c = 0

    for i in range(n):
        if i > c:
            return False

        c = max(c, i + arr[i])

    return True