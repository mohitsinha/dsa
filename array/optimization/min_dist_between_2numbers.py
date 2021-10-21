arr=[2, 5, 3, 5, 4, 4, 2,3 ]
x,y  = 3, 2

x_found = False

y_found = False

res =len(arr)

last_ind = -1

for i in range(len(arr)):
    print(x_found, y_found, res)
    if arr[i] in [x,y]:
        if arr[i] == x:
            if y_found:
                res = min (res, i- last_ind)
                y_found = False
                x_found = True
                continue
            else:
                x_found = True

        else:
            if x_found:
                res =  min(res, i -last_ind)
                y_found = True
                x_found = False
            else:
                y_found = True
        last_ind = i
print(res)


