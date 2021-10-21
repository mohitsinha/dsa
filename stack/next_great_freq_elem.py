# https://www.geeksforgeeks.org/next-greater-frequency-element/

from collections import defaultdict

arr=[1, 1, 2, 3, 4, 2, 1]

map = defaultdict(lambda : 0)

for i in arr:
    map[i]+=1

output = [-1] * len(arr)

nm=dict()
st=[]

for i in range(len(arr)):
    while len(st) >0 and map[arr[i]] > map[st[-1]]:
        nm[st.pop()] = arr[i]

    st.append(arr[i])

print(nm)
print(st)

for i in range(len(arr)):
    if arr[i] in nm:
        output[i] = nm[arr[i]]

print(output)
