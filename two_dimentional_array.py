###
# @File Name          : two_dimentional_array.py
# @Description        : Write a program which takes 2 digits, X,Y as input and generates a 2-dimensional array.
# @Author             : vidyabhojane1@gmail.com
# Ver       Date            Author      		    Modification
# 1.0    27/06/2020   vidyabhojane1@gmail.com     Initial Version
###

row = int(input("Enter number of rows: "))
column = int(input("Enter number of columns: "))
arr = [[1]*column]*row
print(arr)