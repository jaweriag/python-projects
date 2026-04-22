import pandas as pd

# 1. Define the Class
class Product:
    def __init__(self, prod_id, price):
        self.prod_id = prod_id
        self.price = float(price)

    def apply_discount(self, percent_off):
        self.price = self.price * (1 - (percent_off / 100))

df = pd.read_csv('products.csv')

# 3. Filter for Electronics
df_electronics = df[df['Category'] == 'Electronics'].copy()

# 4. Apply logic using the Product class
updated_prices = []
for index, row in df_electronics.iterrows():
    product_obj = Product(row['Product_ID'], row['Price'])
    product_obj.apply_discount(20)  # 20% discount
    updated_prices.append(product_obj.price)

# 5. Update the DataFrame
df_electronics['Price'] = updated_prices
df_electronics['Promo_Active'] = 'Yes'

# 6. Save File (Handles missing Excel engine gracefully)
try:
    # Note: Requires 'openpyxl' installed (pip install openpyxl)
    df_electronics.to_excel('holiday_promos.xlsx', index=False)
    print("Saved as holiday_promos.xlsx")
except Exception as e:
    df_electronics.to_csv('holiday_promos.csv', index=False)
    print(f"Saved as holiday_promos.csv (Reason: {e})")

print("\nFinal Updated Electronics:")
print(df_electronics)
