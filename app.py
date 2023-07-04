from feature_eng import all_teams_finder, selected_team_matches_id, all_shots
from find_all_matches import find_all_matches
from shot_map_dashboard_creator import shot_dashboard
import streamlit as st
import numpy as np
import base64


st.title("Dashboard Creator (WC 2023 shot map demo version)")

# Find all matches details in df format
df_matches = find_all_matches()

# Find all teasm involved in competition
home_teams, away_teams, all_teams = all_teams_finder(df_matches)

# Allow user to select team
selected_team = st.selectbox('Select a team', all_teams)

# Find matches id in which selected team plays
df_matches_with_selected_team_id = selected_team_matches_id(selected_team, home_teams, away_teams, df_matches)

# Dataframe with all the shots, according to selected parameters
all_shots_df = all_shots(df_matches_with_selected_team_id, selected_team)

# All selectable players list
all_selectable_players = np.sort(all_shots_df["player.name"].unique())

# Allow user to select player
selected_player = st.selectbox('Select a player', all_selectable_players)

    
if st.button("Create Dashboard"):

    dashboard = shot_dashboard(selected_player, selected_team, all_shots_df, background_image_path = "./football pitch.png")
    dashboard.save('dashboard.html')
    
    with open("dashboard.html", 'r') as file:
      html_content = file.read()
        
    b64 = base64.b64encode(html_content.encode()).decode()
    href = f'<a href="data:text/html;base64,{b64}" download="desidered dashboard">Click here to download</a>'

    st.markdown(href, unsafe_allow_html=True)


    



