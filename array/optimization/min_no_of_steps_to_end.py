import math
# https://leetcode.com/problems/jump-game-ii/
# recursion

arr= [1, 3, 5, 8, 9, 2, 6, 7, 6, 8, 9]
# arr=[1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
# arr=[1,0,0]
def count(arr, i, res):

    # print(i,res)
    if i==len(arr)-1:
        return res

    if i>=len(arr):
        return math.inf

    y=math.inf
    for j in range(1, arr[i]+1):
         y=min(count(arr, i+j, res+1), y)

    return -1 if y==math.inf else y

print(count(arr, 0, 0))

# dp

sol=[-1] * len(arr)

sol[-1]=0

for i in reversed(range(len(arr)-1)):
    n = arr[i]
    if n==0:
        sol[i] = math.inf
    i_n = i + n
    if i_n >=len(arr)-1:
        sol[i]=1
    else:
        y = math.inf
        for j in range(i+1, i+1+n):
            y = min(y, sol[j])
            if y==1:
                break
        sol[i] = 1 + y


print (sol)

