names=["John","Samuel","Ramsey","Aggie","Grace","Will"]
#accessing items in a list
print(names)
print(names[0])
print(names[-1])
print(names[2])
print(names[0:4])
fruits=["banana","grapes","apples","pinapple","tomato","watermelon","kiwi"]
print(fruits)
print(fruits[3])
print("my faviourite fruit is;",fruits[5])
print(fruits[5].upper())
print("my faviourite fruit is;",fruits[5].upper())
#adding two lists
vegetables=("carrots","broccoli","spinach","kales","managu")
stationeries=("pencils","pens","ink","paper","rubber")
shoppings=vegetables + stationeries
print(shoppings)
print(shoppings[5])
for vegetable in vegetables:
    print(vegetable)
for shopping in shoppings:
    print(shopping)
print("my names is " + names[2]+ " and my faviourite fruit is " + fruits[5])