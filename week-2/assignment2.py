#banks
#!/usr/bin/env python3
#tax in python
#Name:Ramsey Kobia
#Email:ramseykobia@gmail.com
#date: 18th Feb 2023
#file:assigment2.py

print("               KENYA NATIONAL BANK AND TAXATION AUTHORITY                                   ")
name=input("Enter you first name: ")
s_name=input("Enter your second name: ")
r_name=input("Enter your surname: ")
names=name+" "+s_name+" "+r_name
nat=input("Enter your nationality: ")
id_passp=input("Enter your id or passport number: ")
tel=input("Enter your tellephone number: ")
email=input("Enter your email address: ")
POBox=input("Enter your P.O Box: ")
area=input("Enter your are of residence: ")
marital=input("Enter your marital status: ")
occ=input("Enter your occupation: ")
age=int(input("Enter your age: "))
if (age>=(21)):
    print("YOU ARE ELIGIBLE FOR TAXATION AND BANK LOANS")
else:
    print("YOU ARE NOT ELEGIBLE FOR TAXATION NOR BANK LOANS")
if (age>=(21)):
    a=input("Enter the amount you would wish to borrow: ")
    i=10
    T=5
    interest=(int(a)*(i)*(T))/100
    print("Total interest to be paid: ",interest)
    total=(float(interest)+float(a))
    interest_pm=(total)/60
print("Amount to be paid per month is: ",interest_pm)
print("Total amount to be paid after 5 years is: ",total)
ans_total=("Total amount to be paid after 5 years: ",total)
g_income=int(input("Enter your monthly income: "))
if (g_income<=(15000)):
    print("YOUR MONTHLY INCOME IS TOO LOW TO BE TAXED!")
else: 
  if ((15001)<=g_income<=(100000)):
        r1=10/100
        tax1=((r1)*((g_income)-15000))
        print("Payable tax: ",tax1)
        print("Net income: ",(g_income)-(tax1))
        net_inc=((g_income)-(tax1))
  else:
    if((100001)<=g_income<=(150000)):
        r2=15/100
        tax2=((r2)*((g_income)-100000))
        print("Payable tax: ",tax2)
        print("Net income: ",(g_income)-(tax2))
        net_inc=((g_income)-(tax2))
    else:
     if((150001)<=g_income<=(300000)):
        r3=19/100
        tax3=((r3)*((g_income)-150000))
        print("Payable tax: ",tax3)
        print("Net income: ",(g_income)-(tax3))
        net_inc=((g_income)-(tax3))
     else:
        if(g_income>=(300001)):
         r4=30/100
         tax4=((r4)*((g_income)-300000))
         print("Payable tax: ",tax4)
         print("Net income: ",(g_income)-(tax4))
         net_inc=((g_income)-(tax4))



print("                                       YOUR RECEIPT                                                      ")
print(names)
print(nat)
print(id_passp)
print(tel)
print(email)
print(POBox)
print(area)
print(marital)
print(occ)
print(age)
print("Amount to be borrowed is: ",a)
print("Period given to repay the loan+interest is 5 years.")
print("Interest on loan, to be paid is: ",interest)
print("Amount to be paied per month is: ",interest_pm)
print("Total amount to be paid after 5 years: ",total)
print("Your net income is: ",net_inc)