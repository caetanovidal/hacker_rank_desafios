from salary import Salary



name = input("Name: ")
gross_sal = float(input("Gross salary: "))
tax = float(input("Tax: "))

sal = Salary(name, gross_sal, tax)

print(sal.salary())

incr = float(input("Which percentage to increase salary? "))

print(sal.increase(incr))

