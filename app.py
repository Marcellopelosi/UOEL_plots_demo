from feature_eng import all_teams_finder, selected_team_matches_id, all_shots
from find_all_matches import find_all_matches
from shot_map_dashboard_creator import shot_dashboard
import streamlit as st


def raw_data_to_df(url):
  f = requests.get(url)
  data = f.json()
  df = pd.json_normalize(data)
  return df

class statsbomb:

  def competitions():
    return raw_data_to_df("https://raw.githubusercontent.com/statsbomb/open-data/master/data/competitions.json")

  def matches(competition_id, season_id):
    link = "https://raw.githubusercontent.com/statsbomb/open-data/master/data/matches/" + str(competition_id) + "/" + str(season_id) + ".json"
    return raw_data_to_df(link)

  def events(match_id):
    link = "https://raw.githubusercontent.com/statsbomb/open-data/master/data/events/" + str(match_id) + ".json"
    return raw_data_to_df(link)

def find_all_matches():
  return statsbomb.matches(43,106)

# Retrive the table with all matches listed
df_matches = find_all_matches() 

# Find all teasm involved in competition
home_teams, away_teams, all_teams = all_teams_finder(df_matches)

# Allow user to select team
selected_team = "Uruguay"

# Find matches id in which selected team plays
df_matches_with_selected_team_id = selected_team_matches_id(selected_team, home_teams, away_teams, df_matches)

# Dataframe with all the shots, according to selected parameters
all_shots_df = all_shots(df_matches_with_selected_team_id)

# All selectable players list
all_selectable_players = np.sort(all_shots_df["player.name"].unique())

# Allow user to select player
selected_player = "Edinson Roberto Cavani Gómez"

st.title("File Downloader")

# Button to download file
if st.button("Download Dashboard"):
  dashboard = shot_dashboard(player, squad, df, background_image_path = "./football pitch.png")
  dashboard.save('dashboard.html')
  st.download_button("Click to download", file_name='dashboard.html')






