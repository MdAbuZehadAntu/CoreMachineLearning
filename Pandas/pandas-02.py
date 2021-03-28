from io import StringIO

import pandas as pd
import numpy as np

#reading the train dataset
data=pd.read_csv("train.csv")
print(data.head())

#showing info
# RangeIndex: 4209 entries, 0 to 4208
# Columns: 378 entries, ID to X385
# dtypes: float64(1), int64(369), object(8)
# memory usage: 12.1+ MB
print(data.info())


#describe ,method (only applied for numerical features)
print(data.describe())

#unique category count
print(data['X0'].value_counts())


#a little filtering
print(data[data['y']>200])

# making a string csv
d1=(
    "c1,c2,c3\n"
    "a,b,c\n"
    "a2,b3,c3"
)
print(type(d1))
df=pd.read_csv(StringIO(d1))
print(df)

#reading from specific columns
df=pd.read_csv(StringIO(d1),usecols=[i for i in df.columns if i!="c2"])
print(df)