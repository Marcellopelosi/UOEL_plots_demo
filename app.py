from feature_eng import all_teams_finder, selected_team_matches_id, all_shots
from find_all_matches import find_all_matches
from shot_map_dashboard_creator import shot_dashboard
import streamlit as st


# Find all matches details in df format
df_matches = find_all_matches()

# Find all teasm involved in competition
home_teams, away_teams, all_teams = all_teams_finder(df_matches)

# Allow user to select team
selected_team = "Uruguay"

# Find matches id in which selected team plays
df_matches_with_selected_team_id = selected_team_matches_id(selected_team, home_teams, away_teams, df_matches)

# Dataframe with all the shots, according to selected parameters
all_shots_df = all_shots(df_matches_with_selected_team_id, selected_team)

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






