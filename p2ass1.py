salary = int(input("Enter the salary: "))
if salary < 30000:
    tax = salary*(5/100)
    print(tax)
elif salary > 30000 and salary < 70000:
    tax = salary*(15/100)
    print(tax)
else:
    tax = salary*(25/100)
    print(tax)
