import pandas as pd
df = pd.read_csv("main2.csv")
occupation_groups = df.groupby('occupation').agg({'age': [ 'min', 'max']})
print(occupation_groups)
occupation_groups.to_csv("Answer2.csv")
