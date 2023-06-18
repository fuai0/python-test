import pandas as pd
df = pd.read_csv("Nowcoder.csv")
print(df.iloc[0].isnull())