import pandas as pd
df = pd.read_csv("main1.csv")
decade_groups = df.groupby((df['Year']//10)*10)
aggregate = {"Population": "max", "Violent": "sum", "Property": "sum","Murder":"sum","Forcible_Rape":"sum","Robbery":"sum","Aggravated_assault":"sum","Burglary":"sum","Larceny_Theft":"sum","Vehicle_Theft":"sum"}
grouped_df = decade_groups.aggregate(aggregate)
print(grouped_df)
