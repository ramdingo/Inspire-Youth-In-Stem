#revision001
print("_______________________________________________________________________________________________________")
print("|                                           EQUITY BANK                                                    ")
print("|                                        LOAN APPLICATION                                                  ")
f_name=input("|  Enter your fisrt name:")
s_name=input("|  Enter your second name:")
info=input("|  Enter you id number:")
info=input("|  Enter your telephone number:")
info=input("|  Enter your e-mail address:")
info=input("|  Enter your area of residence:")
info=input("|  Enter your date of birth:")
info=input("|  Enter your marital status:")
info=input("|  Do you have any other outstanding debt? And is so, describe briefly:")
info=input("|  Enter the amount you would wish to borrow:")
info=input("|  What is the purpose of the amount being borrowed?")
#calculation of interest
f_num=input("|  Enter the amount you would wish to borrow:")
i=10
T=4
ans=(int(f_num)*(i)*(T))/100
print("|  Interest to be paid;",ans)
Total=(float(ans)+int(f_num))
print("|  Total amount to be paid;",Total)
message=("|  Thankyou for using Equity services. We will get in touch as soon as we finish processing your request.")
print (message.upper())
print("|__________________________________________________________________________________________________________")