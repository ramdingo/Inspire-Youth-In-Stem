#creat an empty list of faviourite musicians
#using for_loop add 5 new musicians
#copy to a new list called celebs
#sort the list
#pop out two celebs from the list
#count the remaining celebs

myMucisians=[ ]
newmus=["Mbosso","Platnumz","Ibraah","Harmonize","Macvoice","Beyonce"]
for newmu in newmus:
    myMucisians.append(newmu)
    print(myMucisians)
myMucisians.sort()
print(myMucisians)
myMucisians.pop()
myMucisians.pop()
print(myMucisians)
print(len(myMucisians))
