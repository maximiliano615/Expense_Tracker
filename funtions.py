#el siguiente programa podra agregar gastos, actualizar un gasto, eliminar un gasto, ver todos los gastons, 
#ver un resumen de todos los gastos y ver el resumen de los gastos de un solo mes

import pandas as pd
from datetime import datetime 
import os

class expenses:
    def __init__(self,expenses,description,category):
        self.expenses = expenses
        self.description = description
        self.id = 0
        self.category = category

    def id_expenses(self):
        if os.path.exists("expenses.csv"):
            pd_previous = pd.read_csv("expenses.csv")
            id = pd_previous["id"].max() + 1
            return id
        else:
            self.id = 0
            return self.id
        
    def to_dict(self):
        id = int(self.id_expenses())
        time = datetime.today().strftime("%d/%m/%Y")
        expenses = int(self.expenses)
        description = str(self.description)
        diccionario = dict({"id": [id] , "expenses": [expenses] , "description": [description] , "time":[time], "category":[self.category]})
        return diccionario

class save_expenses:
    def save(self,expenses):
        if os.path.exists("expenses.csv"):
            df = pd.DataFrame(expenses)
            df.to_csv("expenses.csv", index=True,mode="a", encoding="utf-8", header=False)
            print("file saved")
        else:
            df = pd.DataFrame(expenses)
            df.to_csv("expenses.csv", index=True, encoding="utf-8")
            print("file saved")

class modify_expenses:
    def modify(self,id,expenses=None,description=None,time=None,category=None):
        if os.path.exists("expenses.csv"):
            df = pd.read_csv("expenses.csv")
            if id in df['id'] and expenses is not None:
                df.loc[df['id']==id,"expenses"] = expenses
                df.to_csv("expenses.csv", index=False,mode="w", encoding="utf-8")
            elif id in df['id'] and description is not None:
                df.loc[df['id']==id,"description"] = description
                df.to_csv("expenses.csv", index=False,mode="w", encoding="utf-8")
            elif id in df['id'] and time is not None:
                df.loc[df['id']==id,"time"] = time
                df.to_csv("expenses.csv", index=False,mode="w", encoding="utf-8")
            elif id in df['id'] and category is not None:
                df.loc[df['id']==id,"category"] = category
                df.to_csv("expenses.csv", index=False,mode="w", encoding="utf-8")
        else:
            print("file not found")

class delete_expenses:
    def delete(self,id):
        if os.path.exists("expenses.csv"):
            df =pd.read_csv("expenses.csv")
            if id in df["id"]:
                print(df.loc[df["id"]==id])
                df.drop(df.loc[df["id"]==id].index , axis=0 , inplace=True)
                df.to_csv("expenses.csv", index=False,mode="w", encoding="utf-8")
            else:
                print("id not found")
        else:
            print("file not found")

class read_expenses:
    def __init__(self,max_expenses_month):
        self.max_expenses_month = max_expenses_month

    def read(self):
        if os.path.exists("expenses.csv"):
            df = pd.read_csv("expenses.csv")
            print(df)
        else:
            print("file not found")
    
    def read_summary_report(self):
        if os.path.exists("expenses.csv"):
            df = pd.read_csv("expenses.csv")
            print(df["expenses"].sum())
        else:
            print("file not found")

    def read_month_report(self,month):
        if os.path.exists("expenses.csv"):
            df = pd.read_csv("expenses.csv")
            filtred = df[df["time"]==month]
            if not filtred.empty:
                suma=df.loc[df["time"]==month]["expenses"].sum()
                return int(suma)
            else:
                print("month not found")
        else:
            print("file not found")

    def verify_expenses_max(self,month):
        if os.path.exists("expenses.csv"):
            df = pd.read_csv("expenses.csv")
            suma = self.read_month_report(month)
            if int(suma) > int(self.max_expenses_month):
                print(f"This is your total spending for the month => {self.read_month_report}")
                print(f"This is your maximum expense per month => {self.max_expenses_month}")
                print("expenses Max limit exceded")
            else:
                resta = int(self.max_expenses_month) - int(self.read_month_report(month))
                print(f"You still have money to spend this month => {resta}" )

    def read_for_categories(self,categories):
        if os.path.exists("expenses.csv"):
            df = pd.read_csv("expenses.csv")
            filtred = df[df["category"]==categories]
            if not filtred.empty:
                print(filtred)
                suma=df.loc[df["category"]==categories]["expenses"].sum()
                print(f"money spent for the category {categories} => {suma}")
            else:
                print("category not found")
        else:
            print("file not found")

#suma = read_expenses().read_summary_report()
#suma = read_expenses(1200).read_month_report("20/06/2025")
#suma = read_expenses(1200).verify_expenses_max("20/06/2025")
#suma = read_expenses(1200).read_for_categories("diversion")

#expenses1 = expenses(100, "comida")
#saved = save_expenses().save(expenses1.to_dict())
        
#expenses2 = expenses(200, "comida")
#saved = save_expenses().save(expenses2.to_dict())

#modifications = modify_expenses().modify(1,expenses=300,description="salida")
#expenses3 = expenses(300, "comida")
#saved = save_expenses().save(expenses3.to_dict())
#modifications = modify_expenses().modify(4,expenses=300,description="salida a comer",time="20/07/2025")

#delete_expenses().delete(1)