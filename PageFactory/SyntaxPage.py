import time
from selenium import webdriver
import pandas as pd
import xlrd

data_file = "C:\\Users\\CorinneJoyceReloj\\PycharmProjects\\SDETBDD\\TestData\\TestData.xlsx"
df1 = pd.read_excel(data_file, sheet_name='Sheet1')
print(df1)

print(df1['userName'])
print(df1['password'])
# workbook = xlrd.open_workbook(data_file)
# worksheet = xlrd.sheet_by_index(0)
# print(worksheet)

# verify dashboard
# PIM
# employee list
# type employeeId=15518
# click search button
# verify the last name and first name
#
# enter admin
# no password
# error message
# verify
#
# no username
# password
# error message
# verify