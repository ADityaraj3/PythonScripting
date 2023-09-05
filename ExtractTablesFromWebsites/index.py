import pandas as pd

simpsons = pd.read_html('https://en.wikipedia.org/wiki/List_of_The_Simpsons_episodes')

# print(len(simpsons))
# print(simpsons[1])

df_premier21 = pd.read_csv('https://www.football-data.co.uk/mmz4281/2122/E0.csv')

print(df_premier21)

