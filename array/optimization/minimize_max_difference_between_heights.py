arr= [1, 10, 14, 14, 14, 15]
k=6
mn = mx = arr[0]
for i in arr:
    mx = max(i, mx)
    mn = min(i, mn)

nmin = mn + k
nmax = mx - k

for i in range(len(arr)):
    num = arr[i]

    if (num + k) - nmax < nmin - (num -k):
        arr[i] = num + k
        nmax = max(nmax, num + k)
    else:
        arr[i] = num - k
        nmin = min(nmin, num - k)



