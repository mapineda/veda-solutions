import requests
from bs4 import BeautifulSoup
import pandas as pd
import re

col_url = "https://www.espn.com/mlb/history/leaders/_/breakdown/season/year/2020/start/1"
# Gets HTML
col_r = requests.get(col_url)
col_soup = BeautifulSoup(col_r.text, "html.parser")

# get header columns and create DataFrame
header = col_soup.find('tr', attrs={'class': 'colhead'})
columns = [col.get_text() for col in header.find_all('td')]

final_df = pd.DataFrame(columns=columns)

# loop through players in table
for i in [1, 51]:
    player_url = f"https://www.espn.com/mlb/history/leaders/_/breakdown/season/year/2020/start/{i}"

    r = requests.get(player_url)
    soup = BeautifulSoup(r.text, "html.parser")

    players = soup.find_all('tr', attrs={'class':re.compile('row player-10-')})
    for player in players:
        stats = [stat.get_text() for stat in player.find_all('td')]
        temp_df = pd.DataFrame(stats).transpose()
        temp_df.columns = columns
        final_df = pd.concat([final_df, temp_df], ignore_index=True)

final_df.to_json(r'./mlb_stats.json', orient='records', lines=True)
