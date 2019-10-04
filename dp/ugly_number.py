n = 150
a=[1,2,3,4,5,6,8]
i=9
while True:
    for j in range(2,int(i/2)+1):
        if i%j ==0 :
            quotient = i // j
            if i==14:
                print(quotient, i, j)
            if quotient in a:
                if i == 14:

                    print('hello', quotient, i, j)
                a.append(i)
            break

    if(len(a)==150):
        break
    i+=1

print(a)
print(a[n-1])