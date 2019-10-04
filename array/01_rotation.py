arr = [1,2,3,4,5,6,7]
d = 3
for i in range(d):
    temp = arr[0]
    for j in range(1,len(arr)):
        arr[j-1] = arr[j]

    arr[-1]=temp

print(arr)

arr = [1,2,3,4,5,6,7]


def gcd(a,b):
    if b==0:
        return a
    return gcd(a,a%b)

for i in range(d):
    length = len(arr)
    g = gcd(length, d)

    temp = arr[i]
    for j in range(g):


print(arr)