import pandas as pd

df = pd.read_excel(r"C:\Users\adity\Desktop\PythonScripting\PythonScripting\pivotTable\supermarket_sales.xlsx")

df = df[['Gender','Product line','Total']]
# print(df)


pivot_table = df.pivot_table(index='Gender',columns='Product line',values='Total',aggfunc='sum').round(0)

# this will tell that how much has each gender spend on each product line.

# print(pivot_table)

pivot_table.to_excel(r"C:\Users\adity\Desktop\PythonScripting\PythonScripting\pivotTable\pivot_table.xlsx",'Report',startrow=4)
