print("Linto Mathew Joy")
print("A24MCA041")
print("Experiment No: 4")

color_list1 = []
color_list2 = []
n = int(input("Enter the limit of colors: "))

print("Enter the 1st color list:")
for i in range(n):
    c = input("Enter the color: ")
    color_list1.append(c)

print("color_list1:", color_list1)
print("The first color in color list 1:", color_list1[0])
print("The last color in color list 1:", color_list1[-1])

print("Enter the 2nd color list:")
for i in range(n):
    c = input("Enter the color: ")
    color_list2.append(c)

print("Colors in color_list1 not in color_list2:")
uniqueList = [x for x in color_list1 if x not in color_list2]
print(uniqueList)

color_code = {
    'red': 1,
    'green': 2,
    'blue': 3,
    'orange': 4,
    'white': 5,
    'yellow': 6,
    'black': 7,
    'purple': 8,
    'pink': 9,
}

color_int = []
for x in color_list1:
    if x in color_code.keys():
        color_int.append(color_code[x])

print("Color code of color_list1:", color_int)
oddColor = [x for x in color_int if x % 2 != 0]
print("Odd colors:", oddColor)
