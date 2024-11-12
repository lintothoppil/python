print("Name: Linto Mathew Joy")
print("Admission No: A24MCA041")
print("Experiment: 5")
fruit = {
'banana': 1,
'apple': 2,
'mango': 3,
'kiwi': 4,
'grape': 5,
}
asc = dict(sorted(fruit.items()))
desc = dict(sorted(fruit.items(), reverse=True))
print("Ascending order:", asc)
print("Descending order:", desc)
merged={**asc,**desc}
print("Merged:", merged)