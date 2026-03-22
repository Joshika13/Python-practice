with open("bata.txt",'r') as f:
    data=f.read()
    words=data.split() 
    freq={}
    for word in words:
       if word in freq:
        freq[word]+=1
       else:
        freq[word]=1
    print(freq)
         
