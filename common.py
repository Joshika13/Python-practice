lst1=map(int,input("enter the values of lst1:").split())
lst2=map(int,input("enter the values of lst2:").split())
uni1=set(lst1)
uni2=set(lst2)
common=uni1 & uni2
print(common)