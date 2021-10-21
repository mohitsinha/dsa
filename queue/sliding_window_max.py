# https://www.geeksforgeeks.org/sliding-window-maximum-maximum-of-all-subarrays-of-size-k/

from collections import deque


arr, k = [8, 5, 10, 7, 9, 4, 15, 12, 90, 13], 4

q = deque()

n = len(arr)

for i in range(k):
    while q and arr[i] >= arr[q[-1]]:
        q.pop()

    q.append(i)

for i in range(k,n):
    print(arr[q[0]])

    while q and q[0]<=i-k:
        q.popleft()

    while q and arr[i]>=arr[q[-1]]:
        q.pop()

    q.append(i)

print(arr[q[0]])