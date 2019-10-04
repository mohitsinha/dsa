import math
arr=[5,6,8]

n = 50
a=[0 for x in range(n+1)]


for i in range(1, n+1):
    if i in arr:
        a[i]=1
        continue

    temp = math.inf
    for j in range(1, int(i/2)+1):
        temp=min(temp, a[j]+a[i-j])

    a[i]=temp
print(a[1:])