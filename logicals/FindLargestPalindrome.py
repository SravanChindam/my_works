lst = ['mom','dad','racecar','liril','malayalam','madam']
d = {}
for word in lst:
    d[word] = len(word)
print(d)
for nname, llen in d.items():
    plist = []
    mpl = max(d.values())
    for xx, yy in d.items():
        if yy == mpl:
            plist.append(xx)
print("Largest palindrome word:",plist)
