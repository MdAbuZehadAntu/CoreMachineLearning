import pandas as pd
import numpy as np

# playing with Dataframe

df = pd.DataFrame(np.arange(0, 20, 1).reshape(4, 5), index=["r1", "r2", "r3", "r4"],
                  columns=["c1", "c2", "c3", "c4", "c5"])
print(df)


# converting into a csv file
df.to_csv("test1.csv", sep="\t", header=None, index=None)

# accessing the elements using loc

# print(df.loc[:, "c1"])

# sum of null values column wise
# print(df.isnull().sum())


# value count-> which data how many times appears

print((df.loc[:, "c1"].value_counts()))

# another way of accessing the column values

# print(df[["c1", "c2"]])

#unique values in a column

print(df["c1"].unique())