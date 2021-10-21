import pandas as pd
df = pd.read_csv("main3.csv")
sorted = df.sort_values(['Red Cards','Yellow Cards'],ascending=[False,False])
print(sorted[['Team','Yellow Cards','Red Cards']])