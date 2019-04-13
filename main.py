import pandas as pd

data = pd.read_csv("C:/Users/ronoy/OneDrive/Documents/forefront/season-1819_csv.csv")
from matplotlib import pyplot as plt
data.head()

liverpool = data[(data.AwayTeam == 'Liverpool') | (data.HomeTeam == 'Liverpool')]    # print matches liverpool has played

liverpool
liverpool.mean()
matchList = []
for i in range(0,len(totalScores)):
    matchList.append(i)


liverpool = liverpool.set_index([matchList])


goalsScoredHome = liverpool['FTHG'][liverpool['HomeTeam'] == 'Liverpool']
goalsScoredAway = liverpool['FTAG'][liverpool['AwayTeam'] == 'Liverpool']
totalScores = goalsScoredHome.append(goalsScoredAway)

#lines = totalScores.plot.line()
plt.plot(totalScores.sort_index())

fig = plt.figure()
plt.plot(totalScores.sort_index())
fig.suptitle('Liverpool Goals Scored 2018/19')
plt.xlabel('Gameweek', fontsize=18)
plt.ylabel('Goals Scored', fontsize=16)

fig.savefig('output.png')
