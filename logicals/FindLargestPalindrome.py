lst = ['mom','dad','racecar','liril','malayalam','madam']
d = {}
for word in lst:
    d[word] = len(word)
print(d)
plist = []
large_word = max(d.values())
for nname, llen in d.items():
    if llen == large_word:
        plist.append(nname)
print("Largest palindrome word:",plist)
