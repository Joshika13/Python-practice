a=[1,1,2,2,3,3,3,4]
freq={}
for i in a :
    if i in freq:
        freq[i]+=1
    else:
        freq[i]=1
max_key=max(freq,key=freq.get)
print(max_key)