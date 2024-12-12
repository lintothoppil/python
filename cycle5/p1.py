print("Name:Linto Mathew Joy")
print("Rollno: 41")
print("Experiment: 15")
f_obj =open("tx.txt","r")
lines= f_obj.readlines()
l1=[line.strip() for line in lines]
print(lines)
print(l1)
