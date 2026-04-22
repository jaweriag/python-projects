import pandas as pd
import os
class Ingredient:
    def __init__(self, name, quantity):
        self.name = name
        self.quantity = float(quantity)

    def use_item(self, amount):
        if self.quantity >= amount:
            self.quantity -= amount
        else:
            print(f"Insufficient stock for {self.name}")

df = pd.read_csv('morning_stock.csv')
df.rename(columns={'Qty_kg': 'Current_Quantity'}, inplace=True)
coffee_row = df[df['Ingredient'] == 'Coffee Beans'].iloc[0]
coffee_obj = Ingredient(coffee_row['Ingredient'], coffee_row['Current_Quantity'])
coffee_obj.use_item(2.5)
df.loc[df['Ingredient'] == 'Coffee Beans', 'Current_Quantity'] = coffee_obj.quantity
df.to_csv('evening_stock.csv', index=False)
print("Updated DataFrame:")
print(df)

