
print("Name: Linto Mathew Joy")
print("Admission No: A24MCA041")
print("Experiment: 3")

# **Finding Factors**
def print_factors(x):
    print(f"The factors of {x} are:")
    for i in range(1, x + 1):
        if x % i == 0:
            print(i)


number = int(input("Enter a number to find its factors: "))
print_factors(number)


#Write lambda functions to find area of square, rectangle and triangle.
l=int(input("length "))
b=int(input("breath :"))
h=int(input("heght:"))
ars=lambda x: x*x
arr=lambda x,y:x*y
art=lambda x,y:0.5*x*y
print("Area of square:",ars(l))
print("Area of rectangle:",arr(l,b))
print("Area of triangle:",art(l,h))