###
# @File Name          : dictionary_employee_salary.py
# @Description        : Write a code that accepts the 2 lists and generates the following result.
#					  :	Employee = [‘Amit’,’Manish’,’Mahi’,’Kirti’,’Mafin’]
#					  :	Salary = [20000,30000,20000,40000,25000]
#					  : Expected result of code: {‘Amit’:20000,’Manish’:30000,’Mahi’:20000,’Kirti’:40000,’Mafin’:25000 }
# @Author             : vidyabhojane1@gmail.com
# Ver       Date            Author      		    Modification
# 1.0    27/06/2020   vidyabhojane1@gmail.com     Initial Version
###

name = input("Enter the employee names separated by space: ")
salary = input("Enter salaries of employees separated by space: ")

emp_name = name.split()
emp_salary = salary.split()

# Printing original keys-value lists
print("Employee List  : " + str(emp_name))
print("Salary List : " + str(emp_salary))

# to convert lists to dictionary
res = {}
for key in emp_name:
    for value in emp_salary:
        res[key] = value
        emp_salary.remove(value)
        break

print("Employee and their respective salary  : " + str(res))
