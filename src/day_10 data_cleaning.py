# task 1

import csv
import pandas as pd
import numpy as np
data1=pd.read_csv("customer_order.csv")
df1=pd.DataFrame(data1)
print("shape before cleaning",df1.shape)
#report missing values
print(df1.isna().sum())
#filling missing values

numeric_cols = df1.select_dtypes(include=[np.number]).columns

df1[numeric_cols] = df1[numeric_cols].fillna(df1[numeric_cols].median())

df1=df1.drop_duplicates()
print("Shape after cleaning",df1.shape)
print(df1)


# task 2

import pandas as pd
data2={
       "Date":["2026-01-01","2026-01-02","2026-01-03","2026-01-04"],
       "Price":["$100.50","$200.75","$300.20","$400.10"]
       }
df2=pd.DataFrame(data2)
print(df2)
#data types
print(df2.dtypes)
#converting data types
df2["Price"]=df2["Price"].str.replace("$","",regex=False).astype(float)#removing dollar
print(df2)
print(df2.dtypes)#changed datatype

df2["Date"]=pd.to_datetime(df2["Date"])
print(df2)
print(df2.dtypes)

# task 3

import pandas as pd
data3={
       "Location":[" New York","new york","NEW YORK ","New York"]
       }
df3=pd.DataFrame(data3)
print(df3)
#before cleaning
df3.groupby("Location").size()
print(df3["Location"].unique())
#cleaning
df3["Location"]=df3["Location"].str.strip()
df3["Location"]=df3["Location"].str.title()#or you can use str.lower
#after cleaning
print(df3["Location"].unique())
df3.groupby("Location").size()