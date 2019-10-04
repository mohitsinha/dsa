arr=[3,5,8,9,10,17,17,20]
a = [0 for i in range(len(arr))]
a[0]=arr[0]
for i in range(len(arr)):
    if i ==0:
        continue
    max_val= 0
    for j in range(i+1):
        max_val = max(max_val, arr[j] + a[i-j-1])
    a[i]=max_val
print(a)