integer=1234
reversed_integer=0
while integer >0:
     digit = integer%10
     reversed_integer=reversed_integer*10+digit
     integer//=10
print(reversed_integer)

        #(OR)

# a= str(integer)
# b=a[::-1]
# print(b)
