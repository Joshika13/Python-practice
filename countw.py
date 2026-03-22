with open ("bata.txt","r") as f:
   data=f.read()
   words=data.split()
   print("number of words:",len(words))
   