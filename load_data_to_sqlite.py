import pandas as pd
import sqlite3
df=pd.read_excel('Christmas_Retail_Sales_and_Marketing_Analysis_Dataset.xlsx')

# Create sqllite database
conn=sqlite3.connect("retail.db")

# write dataframe to sql table
df.to_sql("transactions",conn,if_exists="replace",index=False)

conn.close()

print("Data Loaded sqlite successfully")