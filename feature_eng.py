import pandas as pd
import numpy as np


def all_teams_finder(df_matches):
  ''' returns all teams of the chosen competition '''

  home_teams = df_matches['home_team.home_team_name'].to_list()
  away_teams = df_matches['away_team.away_team_name'].to_list()
  all_teams = list(set(home_teams + away_teams))
  all_teams = np.sort(all_teams)
  return home_teams, away_teams, all_teams

def selected_team_matches_id(selected_team, home_teams, away_teams, df_matches):
  matches_with_selected_team = np.logical_or(np.array(home_teams) == selected_team,np.array(away_teams) == selected_team)
  return df_matches[matches_with_selected_team]["match_id"]

relevant_features = ['period',
 'minute',
 'second',
 'team.name',
 'location',
 'player.name',
 'shot.body_part.name',
 'shot.type.name',
 'shot.outcome.name']


def find_defending_team(teams_involved, attacking_team):
  t = list(teams_involved.copy())
  t.remove(attacking_team)
  return t[0]


def all_shots(df_matches_with_selected_team_id):

  all_shots = []
  for m in df_matches_with_selected_team_id:
    df = statsbomb.events(m)
    teams_involved = df["team.name"].unique()
    df = df[relevant_features].dropna()
    df["squad against"] = df["team.name"].apply(lambda x: find_defending_team(teams_involved, x))
    df["x_loc"] = df["location"].apply(lambda x: x[0])
    df["y_loc"] = df["location"].apply(lambda x: x[1])
    df = df[df["team.name"] == selected_team]
    df = df.drop(columns = ["team.name", "location"])
    df.columns = ['period', 'minute', 'second', 'player.name', 'body part',
        'type of shot', 'shot outcome', 'squad against', 'x_loc',
        'y_loc']
    all_shots.append(df)

  all_shots = pd.concat(all_shots)
  return all_shots
