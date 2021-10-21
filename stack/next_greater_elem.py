# https://www.geeksforgeeks.org/next-greater-element/

arr=[13, 7, 6, 12]
arr=[11, 13, 3, 21]

st=[]
st.append(0)

for i in range(1,len(arr)):
    next = arr[i]
    while len(st)>0 and arr[i] > arr[st[-1]]:
        popped = arr[st.pop()]
        print(popped, ' next ', next)
    st.append(i)


while len(st)>0:
    print(arr[st.pop()], ' next -1')




st=[]
st.append(arr[0])

for i in range(1, len(arr)):
    while len(st)>0 and arr[i] > st[-1]:
        print (st.pop(), 'next ', arr[i])
    st.append(arr[i])

while len(st)>0:
    print(st.pop(),'next -1')