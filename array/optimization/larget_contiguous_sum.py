import math

arr =[-2, -3, 4, -1, -2, 1, 5, -3]

m_here = -math.inf
res = -math.inf

for n in arr:
    m_here = max(n, m_here + n)
    res = max(m_here,res)

print(res)