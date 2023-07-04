import pandas as pd
import requests
import numpy as np

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
