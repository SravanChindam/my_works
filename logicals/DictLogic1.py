
def remove_duplicate_letters():
    d={}
    for i in str:
        if i in d:
            d[i]=d[i]+1
        else:
            d[i]=1
    print(d)
    for k,v in d.items():
        if(v==1):
            print(k, end='')
str = input("enter a string: ")
remove_duplicate_letters()
