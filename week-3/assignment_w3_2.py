#W.A.P that solves quadratic equations
#using for loop
#draw a diamond
#draw a triangle
#pascals triangle

#assignment
#!/usr/bin/env python3
#break in while loop
#Name:Ramsey Kobia
#Email:ramseykobia@gmail.com
#date: 21th Feb 2023
#file:assignment_w3_2.py

a=int(input("Enter the value of a :"))
b=int(input("Enter the value of b :"))
c=int(input("Enter the value of c :"))
x1=((-b)+((b**2)-(4*a*c))**0.5)/(2*a)
x2=((-b)-((b**2)-(4*a*c))**0.5)/(2*a)
print("Value of x1 :",(x1))
print("Value of x2 :",(x2))
#hence the value of y
y1=((a*x1**2)+(b*x1)+(c))
y2=((a*x2**2)+(b*x2)+(c))
print("Value of y1 is: :",(y1))
print("Value of y2 is: :",(y2))

triangles=["   *   ","  ***  "," ***** ","*******"]
for triangle in triangles:
    print(triangle)

diamonds=["   *   ","  ***  "," ***** ","*******"]
for diamond in diamonds:
    print(diamond)
diamonds.pop()
diamonds.reverse()
for diamond in diamonds:
    print(diamond)

