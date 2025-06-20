import pandas as pd
from datetime import datetime 
import os
from funtions import expenses,save_expenses,modify_expenses,delete_expenses,read_expenses

print("Welcome to Expenses Tracker")

print("""choose an option:
1 - add expenses
2 - modify expenses
3 - delete expenses
4 - read expenses
5 - read summary report
6 - read month report
7 - verify for category
8 - verify expenses max
9 - modify max expenses per month
10 - exit
""")

max_expenses_month = 2000

def option_validator(option):
    try:
        option = int(option)
        return int(option)
    except:
        print("invalid option. please choose numeric value")

option = 0
while option != 10:
    option = option_validator(input("please choose an option => "))
    if option == 1:
        expenses_input = int(input("expenses => "))
        description = input("description => ")
        category = input("category => ")
        add_expenses = expenses(expenses_input,description,category)
        saved = save_expenses().save(add_expenses.to_dict())
        print("expenses added")
    elif option == 2:
        print("please enter the id of the expense to modify")
        id = int(input("id => "))
        print("If you don't have to modify any object, just press enter.")
        expenses = int(input("expenses => "))
        description = input("description => ")
        category = input("category => ")
        modify_expenses().modify(id,expenses,description,category)
        print("expenses modified")
    elif option == 3:
        print("please enter the id of the expense to delete")
        id = int(input("id => "))
        delete_expenses().delete(id)
        print("expenses deleted")
    elif option == 4:
        read_expenses(max_expenses_month).read()
    elif option == 5:
        read_expenses(max_expenses_month).read_summary_report()
    elif option == 6:
        print("please enter the month to read")
        month = input("please enter the day, month and year of the month to read (d/m/y) => ")
        read_expenses(max_expenses_month).read_month_report(month)
    elif option == 7:
        categories = input("please enter the category to read => ")
        read_expenses(max_expenses_month).read_for_categories(categories)   
    elif option == 8:
        print("please enter the month to verify")
        month = input("please enter the day, month and year of the month to read (d/m/y) => ")
        read_expenses(max_expenses_month).verify_expenses_max(month)
    elif option == 9:
        print("please enter the new maximum expenses per month")
        max_expenses_month = int(input("new maximum expenses per month => "))
        print("expenses max modified")
    elif option == 10:
        print("bye")
        break
    else:
        print("invalid option")
    


