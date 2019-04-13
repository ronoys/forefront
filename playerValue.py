import pandas as pd

df = pd.read_csv("C:/Users/ronoy/OneDrive/Documents/forefront/player_set.csv")

df.head()
print df.max(axis=0)
df.groupby(['Name','Club'], as_index=False)['Appearances'].max()
df[df['Appearances']==df['Appearances'].max()]

longestServing = df.sort_values(['Aerial battles lost'],ascending=[1])
longestServing
newArrivals = df[(df.Appearances < 38) & (df.Appearances > 10)]
newArrivals
