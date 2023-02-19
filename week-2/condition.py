age=59
gender="male"
if (age<18):
    print("you are still young")
else:
    print("you should get an id")
#compound/multiple conditions
if(age>30) & (gender=="male"):
    print("you qualify for a loan")
else:
    print("no loan for you")
#either conditions
age=int(input("enter your age"))
gender=input("enter your gender")
if((age<=31) | (gender=="male")):
    print("you qualify")
else:
    print("you do not qualify")

   