import math

arr=[-2, -3, 4, -1, -2, 1, 5, -3]

sum = arr[0]
m_here = arr[0]

for i in range(len(arr)):
    n=arr[i]

    m_here = max(n, m_here+n)
    sum = max(m_here, sum)
print(sum)

