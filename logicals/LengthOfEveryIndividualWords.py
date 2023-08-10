sentence = input("enter a sentence : ")
print("Given sentence is :",sentence)
words = sentence.split()
print("Given words are : ",words)
for i in words:
    print("{}\t\t{}".format(len(i),i))