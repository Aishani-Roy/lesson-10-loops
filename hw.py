base=int(input("enter your base"))
exponent=int(input("enter your exponent"))
result=1
for i in range(1,exponent+1):
    result=result*base
print(base,"to the power of",exponent,"is",result)    