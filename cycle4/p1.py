class Rectangle:

    def __init__(self, l, b):
        self.length = l
        self.breadth = b

    def perimeter(self):
        return 2 * (self.length + self.breadth)

    def area(self):
        return self.length * self.breadth

    def compare(self, r2):
        try:
            if r2.area() > self.area():
                print("Area of rectangle 2 is greater")
            elif r2.area() < self.area():
                print("Area of rectangle 1 is greater")
            else:
                print("Both areas are equal")
        except Exception as e:
            print(f"Error during comparison: {e}")


print("\nLinto Mathew Joy")
print("Rollno:41")
print("Experiment:11")

try:
    print("Enter dimensions for the first rectangle:")
    length1 = float(input("Enter length of rectangle 1: "))
    breadth1 = float(input("Enter breadth of rectangle 1: "))

    print("\nEnter dimensions for the second rectangle:")
    length2 = float(input("Enter length of rectangle 2: "))
    breadth2 = float(input("Enter breadth of rectangle 2: "))

    r = Rectangle(length1, breadth1)
    r2 = Rectangle(length2, breadth2)

    print("\nArea of 1st rectangle:", r.area())
    print("Perimeter of 1st rectangle:", r.perimeter())

    print("\nArea of 2nd rectangle:", r2.area())
    print("Perimeter of 2nd rectangle:", r2.perimeter())

    print()
    r.compare(r2)

except ValueError as e:
    print(f"Invalid input: {e}. Please enter numeric values only.")
except Exception as e:
    print(f"An unexpected error occurred: {e}")
