###
# @File Name          : printing_star_pattern.py
# @Description        : Write a code that generates the following pattern based on True or False conditions
# @Author             : vidyabhojane1@gmail.com
# Ver       Date            Author      		    Modification
# 1.0    27/06/2020   vidyabhojane1@gmail.com     Initial Version
###

condition = input("Enter Condition (True OR False): ")

if(condition == "false") or (condition == "False"):

    rows = 4
    k = 2 * rows - 2
    for i in range(rows, -1, -1):
        for j in range(k, -1, -1):
            print(end=" ")
        k = k + 1
        for j in range(0, 2 * i + 1):
            print("*", end="")
        print()

else:
    num = 5
    for i in range(0, num):
        for j in range(0, num - i - 1):
            print(end=" ")
        for j in range(0, 2 * i + 1):
            print("*", end="")
        print()

