prices = [7,1,5,3,6,4]

prices=[90,80,70,50]
prof=0


min = prices[0]

for n in prices:
    if (n-min) > prof:
        prof = n-min
    if n<min:
        min=n

print(prof)