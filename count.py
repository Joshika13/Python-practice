string="hello"
freq={}
for ch in string:
    if ch in freq:
        freq[ch]+=1
    else:
        freq[ch]=1
print(freq)