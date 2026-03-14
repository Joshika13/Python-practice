lst=list(map(int,input("enter values:").split()))
largest=lst[0]
for i in lst:
    if i>largest:
        largest=i
print(largest)      