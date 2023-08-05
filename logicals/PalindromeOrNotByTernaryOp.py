word = input("enter any word : ")
output = "Palindrome" if word == word[::-1] else "Not palindrome"
print("__________________________________")
print("given word is ",output)
print("__________________________________")
