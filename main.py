import numpy as np
import pandas as pd
import seaborn as sns
import plotly.plotly as py
from plotly.offline import init_notebook_mode,iplot
import plotly.graph_objs as go
#from wordcloud import WordCloud
import matplotlib.pyplot as plt
import pandas as pd

data = pd.read_csv("C:/Users/ronoy/OneDrive/Documents/forefront/season-1819_csv.csv")

data.head()

homeWins = data['AwayTeam'] [(data['HomeTeam'] == 'Liverpool') & (data['FTR'] == 'H')] # print matches liverpool has won
homeWins
for i in homeWins:
    if i != 'Brighton':
        print i
