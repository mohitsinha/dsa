arr=[1,3,5,7,3,6,4,7]
k=4

wind = sum([arr[i] for i in range(k)])
maxwind=wind

for i in range(len(arr) - k):
    wind = wind + arr[i+k] - arr[i]
    maxwind = max(wind, maxwind)


print(maxwind)