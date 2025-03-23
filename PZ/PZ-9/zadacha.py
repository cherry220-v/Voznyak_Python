def maskify(s:str): return "#"*len(s[:-4])+s[-4:]
cardNum = input("")
print(maskify(cardNum))