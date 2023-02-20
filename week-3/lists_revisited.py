#naming convention
#!/usr/bin/env python3
#tax in python
#Name:Ramsey Kobia
#Email:ramseykobia@gmail.com
#date: 18th Feb 2023
#file:lists_revisited.py

myFaviouriteFruit=["banana","mango","kiwi","pears","oranges","avocado","pinapples"]
for fruit in myFaviouriteFruit:
    print(fruit)
print(len(myFaviouriteFruit))

friends=["Ramsey","Agnes","Samuel","Sos","Chris","Maxime","Shiro"]
print(friends)
friends[0]="Mary"
print(friends)

newFriends=friends.copy()
print(newFriends)
newFriends.sort()
print(newFriends)
newFriends.pop()
print(newFriends)
