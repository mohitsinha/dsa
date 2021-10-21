# https://www.geeksforgeeks.org/find-a-tour-that-visits-all-stations/

from collections import deque

arr = [(4,6), (6,5), (7,3), (4,5)]

n = len(arr)

tot = 0
l = 0
deficit = 0

for i in range(n):
    tot += arr[i][0] - arr[i][1]

    if tot<0:
        l+=1
        tot=0
        deficit+=tot

ans = l if tot+deficit>=0  else -1

print(ans)