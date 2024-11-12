print("Linto Mathew Joy")
print("A24MCA041")
print("Experiment No: 1")
day = int(input("Enter day : "))
month = int(input("Enter month: "))
year = int(input("Enter year: "))
print(f"The date is: {day:02d}-{month:02d}-{year}")
if year % 4==0 and year%100!=0 or year % 400==0:
 print(year,"leap year")
else:
 print(year,"not a leap year")