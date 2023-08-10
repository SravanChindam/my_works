
def remove_duplicates(strngg):
    a = set(strngg)
    a = "".join(a)
    dup = ""
    for i in strngg:
        if i in dup:
            pass
        else:
            dup =dup+i
    print("after removing: {}".format(dup))

strngg = input("enter a string: ")
print("Given sring :",strngg)
remove_duplicates(strngg)


