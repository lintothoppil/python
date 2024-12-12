print("Name: Linto Mathew Joy")
print("Rollno:41")
print("Experiment:13")

class Rectangle:
    def __init__(self, length, width):
        self.__length = length
        self.__width = width

    def area(self):
        return self.__length * self.__width

    def __lt__(self, other):
        if not isinstance(other, Rectangle):
            raise ValueError("Can only compare with another Rectangle")
        return self.area() < other.area()

    def display(self):
        print(f"Rectangle (Length: {self.__length}, Width: {self.__width}, Area: {self.area()})")

try:
    print("Enter dimensions of the first rectangle:")
    length1 = float(input("Length: "))
    width1 = float(input("Width: "))
    rect1 = Rectangle(length1, width1)

    print("\nEnter dimensions of the second rectangle:")
    length2 = float(input("Length: "))
    width2 = float(input("Width: "))
    rect2 = Rectangle(length2, width2)

    print("\nDetails of the rectangles:")
    rect1.display()
    rect2.display()

    print("\nComparing areas:")
    if rect1 < rect2:
        print("The first rectangle is smaller in area.")
    else:
        print("The second rectangle is smaller in area or they are equal.")

except ValueError as e:
    print(f"Invalid input: {e}")
