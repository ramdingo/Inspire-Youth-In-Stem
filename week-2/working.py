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
print(net_inc)
