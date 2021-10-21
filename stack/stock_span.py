price = [100, 80, 60, 70, 60, 75, 85]

st = []

span =[None] * len(price)
span[0]=1
st.append(0)

for i in range(1, len(price)):
    while (len(st)>=0 and price[st[-1]]<=price[i]):
        st.pop()

    span[i] = i+1 if len(st)<=0 else i-st[-1]
    st.append(i)

# print(span)

