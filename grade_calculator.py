name = input("enter name:")

python = float(input("enter python marks:"))
java = float(input("enter java marks:"))
dbms = float(input("enter dbms marks:"))

total = python+java+dbms
average = total/3

print("\n=========student details========")
print("name:",name)
print("total",total)
print("average:",average)

if average >= 90:
    print("Grade:A")
elif average >= 75:
    print("Grade:B")
elif average >= 60:
    print("Grade:C")
elif average >= 35:
    print("Grade:D")
else:
    print("Result:Fail")
