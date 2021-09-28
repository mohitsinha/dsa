arr = [1,2,3,4,5,6,7,8]
d = 3
for i in range(d):
    temp = arr[0]
    for j in range(1,len(arr)):
        arr[j-1] = arr[j]

    arr[-1]=temp

print(arr)

print("///////")
arr = [1,2,3,4,5,6,7,8]

def gcd(a,b):
    if a%b==0:
        return b
    return gcd(b, a%b)

g_c_d = gcd(len(arr), d)
for i in range(0, g_c_d):
    temp = arr[i]

    j=i
    k=j+d
    while k!=i:
        arr[j]=arr[k]
        j=k
        k = (j + d) % len(arr)
    arr[j] = temp

print(arr)
print ('////')
arr = [1,2,3,4,5,6,7,8]

def rev(arr,start, end):

    while start<end:
        t=arr[start]
        arr[start] =arr[end]
        arr[end]=t
        start +=1
        end -=1

rev(arr,0,2)
print(arr)
rev(arr,3,7)
print(arr)

rev(arr,0,7)
print(arr)

print ('////')
arr = [1,2,3,4,5,6,7,8]

# rotate right
temp = arr[-1]
for i in range(len(arr)-1,0, -1):
    arr[i] = arr[i-1]

arr[0] = temp

print(arr)

