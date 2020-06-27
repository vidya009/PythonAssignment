###
# @File Name          : ancient_chinese_puzzle.py
# @Description        : Write a snippet that resolves ancient Chinese puzzle
#					  : We count 35 heads and 94 legs among the chickens and rabbits in a farm. How many
#					  : rabbits and how many chickens do we have?
# @Author             : vidyabhojane1@gmail.com
# Ver       Date            Author      		    Modification
# 1.0    27/06/2020   vidyabhojane1@gmail.com     Initial Version
###

heads = int(input('Enter the total number of heads:'))
legs = int(input('Enter the total number of legs:'))
if legs % 2 != 0 or heads == 0 or heads > legs:
    print("No solution !!!")
else:
    r = int((legs + (-2 * heads)) / 2)
    c = int(heads - r)
    print('Total number of chickens and rabbits respectively: ')
    print('{} {}'.format(c, r))
