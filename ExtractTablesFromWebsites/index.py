import pandas as pd
import os as os
simpsons = pd.read_html('https://en.wikipedia.org/wiki/List_of_The_Simpsons_episodes')
# results list of all the tables


current_directory = os.getcwd()

# List all files in the current directory
files = os.listdir(current_directory)

# Print the list of files
print("Files in the current directory:")
for file in files:
    print(file)

    
# print(len(simpsons))
# print(simpsons[1])

df_premier21 = pd.read_csv('https://www.football-data.co.uk/mmz4281/2122/E0.csv')
# this reads the csv file that is in the link

# print(df_premier21)


#remaning coloums

df_premier21.rename(columns={'FTHG':'Final_Time_Home_Goal',
                              'FTAG':'away_goals'}, inplace=True)

print(df_premier21)


