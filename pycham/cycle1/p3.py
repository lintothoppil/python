print("Linto Mathew Joy")
print("A24MCA041")
print("Experiment No: 3")

a = int(input("Enter the 1st number: "))
b = int(input("Enter the 2nd number: "))
c = int(input("Enter the 3rd number: "))

if a > b:
    if a > c:
        print(a, "is greater")
        n = a
    else:
        print(c, "is greater")
        n = c
else:
    if b > c:
        print(b, "is greater")
        n = b
    else:
        print(c, "is greater")
        n = c

nn = int(f"{n}{n}")
nnn = int(f"{n}{n}{n}")
result = n + nn + nnn
print("The result of n + nn + nnn is:", result)

area = 3.14 * n * n
peri = 2 * 3.14 * n
print("The area of the circle with radius", n, "is:", area)
print("The perimeter of the circle with radius", n, "is:", peri)

vol = (4 / 3) * 3.14 * (n ** 3)
print("Volume of the sphere:", vol)
