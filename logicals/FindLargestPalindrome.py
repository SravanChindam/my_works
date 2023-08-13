lst = ['mom','dad','racecar','liril','malayalam','madam']
d = {}
for word in lst:
    d[word] = len(word)
print(d)
plist = []
for nname, llen in d.items():
    if llen == max(d.values()):
        plist.append(nname)
print("Largest palindrome word:",plist)
