print("Name:Linto Mathew Joy")
print("Rollno: 41")
print("Experiment: 17")
import csv
file_name = 'fav.csv'
with open(file_name, 'r') as csv_file:
    reader = csv.reader(csv_file)
    for row in reader:
        print(row)
