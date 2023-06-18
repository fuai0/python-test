import pandas as pd
df = pd.read_csv("Nowcoder.csv",dtype = object)
print(df.loc[df["Language"]=="Python"])
