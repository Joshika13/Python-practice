list=list(map(int,input("enter the marks:").split()))
print("Marks:",list)
print("highest marks:",max(list))
print("lowest marks:",min(list))
print("average marks:",sum(list)/len(list))
#student performance
count=0
for mark in list:
    if mark>40:
        count+=1
print("Students passed:",count)
failed=len(list)-count
print("Students failed:",failed)
freq={}
for mark in list:
    if mark in freq:
        freq[mark]+=1
    else:
        freq[mark]=1
print("frequency of marks:",freq)
most_freq=max(freq,key=freq.get)
print("Most frequent mark:",most_freq)