#el siguiente programa podra agregar gastos, actualizar un gasto, eliminar un gasto, ver todos los gastons, 
#ver un resumen de todos los gastos y ver el resumen de los gastos de un solo mes

import pandas as pd
from datetime import datetime 
import os
class expenses:
    def __init__(self,expenses,description):
        self.expenses = expenses
        self.description = description
        self.id = 0

    def id_expenses(self):
        if os.path.exists("expenses.csv"):
            pd_previous = pd.read_csv("expenses.csv")
            print(pd_previous["id"].max())
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
        diccionario = dict({"id": [id] , "expenses": [expenses] , "description": [description] , "time":[time]})
        print(type(diccionario))
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

expenses1 = expenses(100, "comida")
saved = save_expenses().save(expenses1.to_dict())
        
expenses2 = expenses(200, "comida")
saved = save_expenses().save(expenses2.to_dict())

expenses3 = expenses(300, "comida")
saved = save_expenses().save(expenses3.to_dict())