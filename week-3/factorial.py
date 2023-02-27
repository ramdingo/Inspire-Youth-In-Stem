#factorials
#example...
print("factorial of 6")
six=6*5*4*3*2*1
print(six)

def factorials(num):
    factorial=1
    if num<0:
        print("NEGATIVE NUMBERS DO NOT APPLY!")
    elif num<2:
        print("{}! is 1".format(num))
    else:
        for numb in range(num,1,-1):
             factorial=factorial*numb
        print(factorial)

factorials(3)

def simpleInterest(amt):
    r=4
    t=5
    interest=(int(amt)*(r)*(t))/100
    total_amt=amt+interest
    print("{} is the input amount. ".format(amt))
    print("Total amount to be paid is: {}".format(total_amt))

simpleInterest(20000)





    
     




