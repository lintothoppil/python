print("Name:Linto Mathew Joy")
print("Rollno: 41")
print("Experiment: 18")
import csv
with open('stud.csv','r') as csv_f:
    csv_r =csv.DictReader(csv_f)
    print("RollNO  Name")
    print("---------------------------------")
    for line in csv_r:
        print(line['Roll No'],"",line['Student Name'])