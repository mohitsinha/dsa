arr = [10, 80, 12, 5, 92, 50, 112, 5]
# arr = [6, 5, 4, 3, 2, 1]
# once

min_p = arr[0]
res = 0
for i in arr:
    res = max(res, i - min_p)
    min_p = min(min_p, i)

print(res)


# Once reversed
arr = [10, 80, 12, 5, 92, 50, 112, 5]
n=len(arr)
max_n=arr[n-1]
res = 0
for i in reversed(range(n)):
    res = max(res, max_n - arr[i])
    max_n=max(arr[i], max_n)


print(res)
# infinite
arr = [10, 80, 12, 5, 92, 50, 112, 5]

res = 0
curr=0
m_p = arr[0]
for i in arr:
    margin = i - m_p
    if margin<curr:
        m_p=i
        res+=curr
        curr = 0
    else:
        curr=margin

print(res)

arr = [10, 80, 12, 5, 92, 50, 112, 5]
res = 0
for i in range(len(arr)-1):
    margin = arr[i+1] - arr[i]
    if margin > 0:
        res += margin
print(res)


# twice two arrays
arr = [10, 80, 12, 5, 92, 50, 112, 5]

n=len(arr)

left_profit = [0]*n
right_profit = [0]*n

min_n = arr[0]
left_profit[0]=0
for i in range(1, n):
    left_profit[i] = max(left_profit[i-1], arr[i] - min_n)
    min_n=min(min_n, arr[i])

print(left_profit)


max_n = arr[n-1]
right_profit[n-1] = 0

for i in reversed(range(0, n-1)):
    right_profit[i] = max(right_profit[i+1], max_n - arr[i])
    max_n = max(max_n, arr[i])

print(right_profit)

res = 0
for i in range(n-1):
    res = max(res, left_profit[i]+right_profit[i+1])
print(res)

# twice one array

arr = [10, 80, 12, 5, 92, 50, 112, 5]
n=len(arr)
profit = [0]*n

min_n = arr[0]
max_n = arr[n-1]
profit[0]=0

for i in reversed(range(0, n - 1)):
    profit[i] = max(profit[i+1], max_n - arr[i])
    max_n = max(max_n, arr[i])


for i in range(1,n):
    profit[i] = max(profit[i-1], profit[i]+ arr[i]-min_n)
    min_n = min(min_n, arr[i])

print(profit[n-1])

