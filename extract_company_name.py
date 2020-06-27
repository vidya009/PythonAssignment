# @File Name          : extract_company_name.py
# @Description        : Assume some email address like "username@companyname.com",
#                     : now write a snippet that extracts the company name of a given email address.
# @Author             : vidyabhojane1@gmail.com
# Ver       Date            Author      		    Modification
# 1.0    27/06/2020   vidyabhojane1@gmail.com     Initial Version
###

import re

email = input("Enter your Email: ")
x = re.findall(r"\@(.*?)\.", email)
print("Your company name is: " + x[0])
