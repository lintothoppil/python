#Program to find the factorial of a number
fact=1
n=int(input("Enter the number:"))
if n == 0:
    print("factorial of",n,"is:",fact)
else:
    for i in range(1,n+1):
        fact=fact*i
    print("factorial of",n,"is:",fact)


#Generate Fibonacci series of N terms
num = int(input("Enter the number:"))
n1, n2 = 0, 1
print("Fibonacci Series:", n1, n2, end=" ")
for i in range(2, num):
    n3 = n1 + n2
    n1 = n2
    n2 = n3
    print(n3, end=" ")

list1 = []
n = int(input("Enter the limit of list: "))
print("Enter the list:")
for i in range(n):
  c = int(input())
  list1.append(c)
print("The Entered list is:", list1)
result = sum(list1)

print("The sum of the list:", result)

def is_all_even_digits(n):
    return all(int(digit) % 2 == 0 for digit in str(n))

def generate_even_digit_squares(start, end):
    results = []
    for i in range(int(start ** 0.5), int(end ** 0.5) + 1):
        square = i * i
        if start <= square <= end and is_all_even_digits(square):
            results.append(square)
    return results

start_range = 1000
end_range = 9999
even_digit_squares = generate_even_digit_squares(start_range, end_range)
print("Even digit squares:", even_digit_squares)
