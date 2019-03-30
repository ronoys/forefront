import numpy as np
import pandas as pd
import seaborn as sns
import plotly.plotly as py
from plotly.offline import init_notebook_mode,iplot
import plotly.graph_objs as go
#from wordcloud import WordCloud
import matplotlib.pyplot as plt
import pandas as pd

cards = pd.read_csv("C:/Users/ronoy/OneDrive/Documents/forefront/kaggle set/card_detail.csv")

print cards.head()
ind_match     = cards.columns.get_loc("id")
ind_league     = matches.columns.get_loc("league_id")
ind_season     = matches.columns.get_loc("season")
ind_stage      = matches.columns.get_loc("stage")
# home team information
ind_h_team     = matches.columns.get_loc("home_team_api_id")
ind_h_player   = matches.columns.get_loc("home_player_1")
ind_h_player_x = matches.columns.get_loc("home_player_X1")
ind_h_player_y = matches.columns.get_loc("home_player_Y1")
# away team information
ind_a_team     = matches.columns.get_loc("away_team_api_id")
ind_a_player   = matches.columns.get_loc("away_player_1")
ind_a_player_x = matches.columns.get_loc("away_player_X1")
ind_a_player_y = matches.columns.get_loc("away_player_Y1")
