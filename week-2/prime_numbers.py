#prime numbers
num=int(input("Enter a number"))
for i in range(2,num):
   if num%i==0:
      break
if i+1==num:
   print(num, "is a prime number")
else:
   print(num, "is not a prime number")
#method two
num=12
for i in range(2,num):
   if num%i==0:
    print(" not prime")
   break
else:
   print("prime")
   