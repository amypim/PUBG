# # -*- coding: utf-8 -*-
# """
# Created on Thu Apr 22 15:53:04 2021

# @author: WIN 10
# """

import pandas as pd
import numpy as np

path = "D:/amy/data vis/project/"

agg_match_stats_0 = pd.read_csv(path + "aggregate/agg_match_stats_0.csv")
agg_match_stats_1 = pd.read_csv(path + "aggregate/agg_match_stats_1.csv")
agg_match_stats_2 = pd.read_csv(path + "aggregate/agg_match_stats_2.csv")
agg_match_stats_3 = pd.read_csv(path + "aggregate/agg_match_stats_3.csv")
agg_match_stats_4 = pd.read_csv(path + "aggregate/agg_match_stats_4.csv")

# # agg_match_stats_0.info()
# head0 = pd.DataFrame(agg_match_stats_0.head())

# party_size = agg_match_stats_0['party_size'].value_counts() 
# player_kills = agg_match_stats_0['player_kills'].value_counts()
# party_size_player_kills = agg_match_stats_0[['party_size','player_kills']].value_counts()
# win0 = agg_match_stats_0.loc[(agg_match_stats_0['team_placement'] == 1)]
# head_win0 = win0.head(100)



### distance ###

## team1 ##
team1 = pd.concat([agg_match_stats_0.loc[(agg_match_stats_0['party_size'] == 1)],
                    agg_match_stats_1.loc[(agg_match_stats_1['party_size'] == 1)],
                    agg_match_stats_2.loc[(agg_match_stats_2['party_size'] == 1)],
                    agg_match_stats_3.loc[(agg_match_stats_3['party_size'] == 1)],
                    agg_match_stats_4.loc[(agg_match_stats_4['party_size'] == 1)]])
team1 = team1[['player_dist_ride','player_dist_walk','player_survive_time','team_placement']]
team1['sum_distance'] = team1['player_dist_ride'] + team1['player_dist_walk']
team1['percent_ride'] = team1['player_dist_ride']/team1['sum_distance']
team1['percent_walk'] = team1['player_dist_walk']/team1['sum_distance']
team1['percent_walk'] = team1['percent_walk'].round(decimals=4)
team1['percent_ride'] = team1['percent_ride'].round(decimals=4)
team1['player_survive_time'] = team1['player_survive_time'].round(decimals=0)

head_team1 = team1.head()

# find outliers for player_survive_time
np.percentile(team1.player_survive_time, [25, 50, 75])
# array([ 207,  578, 1179])
# IQR = Q3 - Q1 = 1179-207 = 972
print(1179-207)
# lower outlier = Q1 - (1.5*IQR) = 207-(1.5*972) = -1251
print(207-(1.5*972))
# upper outlier = Q3 + (1.5*IQR) = 1179+(1.5*972) = 2637
print(1179+(1.5*972))
# lower outlier = -1251 
# upper outlier = 2637

team1 = team1[team1['player_survive_time'] < 2637]

# # team1.to_csv(r'D:/amy/data vis/project/team1_distance.csv')

## team2 ##
team2 = pd.concat([agg_match_stats_0.loc[(agg_match_stats_0['party_size'] == 2)],
                    agg_match_stats_1.loc[(agg_match_stats_1['party_size'] == 2)],
                    agg_match_stats_2.loc[(agg_match_stats_2['party_size'] == 2)],
                    agg_match_stats_3.loc[(agg_match_stats_3['party_size'] == 2)],
                    agg_match_stats_4.loc[(agg_match_stats_4['party_size'] == 2)]])
team2 = team2[['player_dist_ride','player_dist_walk','player_survive_time','team_placement']]
team2['sum_distance'] = team2['player_dist_ride'] + team2['player_dist_walk']
team2['percent_ride'] = team2['player_dist_ride']/team2['sum_distance']
team2['percent_walk'] = team2['player_dist_walk']/team2['sum_distance']
team2['percent_walk'] = team2['percent_walk'].round(decimals=4)
team2['percent_ride'] = team2['percent_ride'].round(decimals=4)
team2['player_survive_time'] = team2['player_survive_time'].round(decimals=0)

head_team2 = team2.head()

# find outliers for player_survive_time
np.percentile(team2.player_survive_time, [25, 50, 75])
# array([ 233.,  620., 1260.])# # IQR = Q3 - Q1 = 1027
print(1260-233)
# # lower outlier = Q2 - (1.5*IQR) = 233-(1.5*1027) = -1307.5
print(233-(1.5*1027))
# upper outlier = Q3 + (1.5*IQR) = 1260+(1.5*1027) = 2800.5
print(1260+(1.5*1027))
# lower outlier = -1307.5
# # upper outlier = 2800.5

team2 = team2[team2['player_survive_time'] < 2800.5]

# team2.to_csv(r'D:/amy/data vis/project/team2_distance.csv')

## team4 ##
team4 = pd.concat([agg_match_stats_0.loc[(agg_match_stats_0['party_size'] == 4)],
                    agg_match_stats_1.loc[(agg_match_stats_1['party_size'] == 4)],
                    agg_match_stats_2.loc[(agg_match_stats_2['party_size'] == 4)],
                    agg_match_stats_3.loc[(agg_match_stats_3['party_size'] == 4)],
                    agg_match_stats_4.loc[(agg_match_stats_4['party_size'] == 4)]])
team4 = team4[['player_dist_ride','player_dist_walk','player_survive_time','team_placement']]
team4['sum_distance'] = team4['player_dist_ride'] + team4['player_dist_walk']
team4['percent_ride'] = team4['player_dist_ride']/team4['sum_distance']
team4['percent_walk'] = team4['player_dist_walk']/team4['sum_distance']
team4['percent_walk'] = team4['percent_walk'].round(decimals=4)
team4['percent_ride'] = team4['percent_ride'].round(decimals=4)
team4['player_survive_time'] = team4['player_survive_time'].round(decimals=0)

head_team4 = team4.head()

# find outliers for player_survive_time
np.percentile(team4.player_survive_time, [25, 50, 75])
# array([ 276.,  714., 1366.])
print(1366-276)
# # lower outlier = Q4 - (1.5*IQR) = 276-(1.5*1090) = -1359
print(276-(1.5*1090))
# upper outlier = Q3 + (1.5*IQR) = 1466+(1.5*1090) = 3101
print(1466+(1.5*1090))
# lower outlier = -1359
# # upper outlier = 3101

team4 = team4[team4['player_survive_time'] < 3101]

# team4.to_csv(r'D:/amy/data vis/project/team4_distance.csv')



### heatmap of most kill area ###

kill_match_stats_final_0 = pd.read_csv(path + "deaths/kill_match_stats_final_0.csv")
kill_match_stats_final_1 = pd.read_csv(path + "deaths/kill_match_stats_final_1.csv")
kill_match_stats_final_2 = pd.read_csv(path + "deaths/kill_match_stats_final_2.csv")
kill_match_stats_final_3 = pd.read_csv(path + "deaths/kill_match_stats_final_3.csv")
kill_match_stats_final_4 = pd.read_csv(path + "deaths/kill_match_stats_final_4.csv")

head_kill0 = kill_match_stats_final_0.head(100)
# # head_kill.info()
# position = kill_match_stats_final_0[['map','killer_position_x','killer_position_y','victim_position_x','victim_position_y']]
position_kill0 = kill_match_stats_final_0[['map','killer_position_x','killer_position_y']]
position_kill1 = kill_match_stats_final_1[['map','killer_position_x','killer_position_y']]
position_kill2 = kill_match_stats_final_2[['map','killer_position_x','killer_position_y']]
position_kill3 = kill_match_stats_final_3[['map','killer_position_x','killer_position_y']]
position_kill4 = kill_match_stats_final_4[['map','killer_position_x','killer_position_y']]

#kill0
position_kill0['killer_position_x'] = position_kill0['killer_position_x'].div(1000).round(decimals=0)
position_kill0['killer_position_y'] = position_kill0['killer_position_y'].div(1000).round(decimals=0)
erangel_kill0 = position_kill0.loc[position_kill0['map'] == 'ERANGEL']
miramar_kill0 = position_kill0.loc[position_kill0['map'] == 'MIRAMAR']
erangel_kill0 = erangel_kill0[['killer_position_x','killer_position_y']].value_counts()
miramar_kill0 = miramar_kill0[['killer_position_x','killer_position_y']].value_counts()

head_miramar_kill0 = miramar_kill0.head()
head_erangel_kill0 = erangel_kill0.head()

# #kill1
position_kill1['killer_position_x'] = position_kill1['killer_position_x'].div(1000).round(decimals=0)
position_kill1['killer_position_y'] = position_kill1['killer_position_y'].div(1000).round(decimals=0)
erangel_kill1 = position_kill1.loc[position_kill1['map'] == 'ERANGEL']
miramar_kill1 = position_kill1.loc[position_kill1['map'] == 'MIRAMAR']
erangel_kill1 = erangel_kill1[['killer_position_x','killer_position_y']].value_counts()
miramar_kill1 = miramar_kill1[['killer_position_x','killer_position_y']].value_counts()

# #kill2
position_kill2['killer_position_x'] = position_kill2['killer_position_x'].div(1000).round(decimals=0)
position_kill2['killer_position_y'] = position_kill2['killer_position_y'].div(1000).round(decimals=0)
erangel_kill2 = position_kill2.loc[position_kill2['map'] == 'ERANGEL']
miramar_kill2 = position_kill2.loc[position_kill2['map'] == 'MIRAMAR']
erangel_kill2 = erangel_kill2[['killer_position_x','killer_position_y']].value_counts()
miramar_kill2 = miramar_kill2[['killer_position_x','killer_position_y']].value_counts()


# #kill3
position_kill3['killer_position_x'] = position_kill3['killer_position_x'].div(1000).round(decimals=0)
position_kill3['killer_position_y'] = position_kill3['killer_position_y'].div(1000).round(decimals=0)
erangel_kill3 = position_kill3.loc[position_kill3['map'] == 'ERANGEL']
miramar_kill3 = position_kill3.loc[position_kill3['map'] == 'MIRAMAR']
erangel_kill3 = erangel_kill3[['killer_position_x','killer_position_y']].value_counts()
miramar_kill3 = miramar_kill3[['killer_position_x','killer_position_y']].value_counts()

# #kill4
position_kill4['killer_position_x'] = position_kill4['killer_position_x'].div(1000).round(decimals=0)
position_kill4['killer_position_y'] = position_kill4['killer_position_y'].div(1000).round(decimals=0)
erangel_kill4 = position_kill4.loc[position_kill4['map'] == 'ERANGEL']
miramar_kill4 = position_kill4.loc[position_kill4['map'] == 'MIRAMAR']
erangel_kill4 = erangel_kill4[['killer_position_x','killer_position_y']].value_counts()
miramar_kill4 = miramar_kill4[['killer_position_x','killer_position_y']].value_counts()

erangel_kill = pd.concat([erangel_kill1, erangel_kill2, erangel_kill3, erangel_kill4])
miramar_kill = pd.concat([miramar_kill1, miramar_kill2, miramar_kill3, miramar_kill4])


# position.to_csv(r'path + position.csv')
erangel_kill.to_csv(r'D:/amy/data vis/project/erangel_kill.csv')
miramar_kill.to_csv(r'D:/amy/data vis/project/miramar_kill.csv')

# # mir = miramar.head()
# # era = erangel.head()
# # # position_group.to_csv(r'path + position_group1.csv')





# ### heatmap for kill area of placement 1 ###

#kill0
winner_kill0 = kill_match_stats_final_0.loc[kill_match_stats_final_0['killer_placement'] == 1]
winner_kill1 = kill_match_stats_final_1.loc[kill_match_stats_final_1['killer_placement'] == 1]
winner_kill2 = kill_match_stats_final_2.loc[kill_match_stats_final_2['killer_placement'] == 1]
winner_kill3 = kill_match_stats_final_3.loc[kill_match_stats_final_3['killer_placement'] == 1]
winner_kill4 = kill_match_stats_final_4.loc[kill_match_stats_final_4['killer_placement'] == 1]

head_winner_kill0 = winner_kill0.head(100)

#kill0
winner_kill0 = kill_match_stats_final_0[['map','killer_position_x','killer_position_y']]
winner_kill0['killer_position_x'] = winner_kill0['killer_position_x'].div(1000).round(decimals=0)
winner_kill0['killer_position_y'] = winner_kill0['killer_position_y'].div(1000).round(decimals=0)
erangel_kill0 = winner_kill0.loc[winner_kill0['map'] == 'ERANGEL']
miramar_kill0 = winner_kill0.loc[winner_kill0['map'] == 'MIRAMAR']
erangel_kill0 = erangel_kill0[['killer_position_x','killer_position_y']].value_counts()
miramar_kill0 = miramar_kill0[['killer_position_x','killer_position_y']].value_counts()

head_miramar_kill0 = miramar_kill0.head(100)

#kill1
winner_kill1 = kill_match_stats_final_1[['map','killer_position_x','killer_position_y']]
winner_kill1['killer_position_x'] = winner_kill1['killer_position_x'].div(1000).round(decimals=0)
winner_kill1['killer_position_y'] = winner_kill1['killer_position_y'].div(1000).round(decimals=0)
erangel_kill1 = winner_kill1.loc[winner_kill1['map'] == 'ERANGEL']
miramar_kill1 = winner_kill1.loc[winner_kill1['map'] == 'MIRAMAR']
erangel_kill1 = erangel_kill1[['killer_position_x','killer_position_y']].value_counts()
miramar_kill1 = miramar_kill1[['killer_position_x','killer_position_y']].value_counts()

#kill2
winner_kill2 = kill_match_stats_final_2[['map','killer_position_x','killer_position_y']]
winner_kill2['killer_position_x'] = winner_kill2['killer_position_x'].div(1000).round(decimals=0)
winner_kill2['killer_position_y'] = winner_kill2['killer_position_y'].div(1000).round(decimals=0)
erangel_kill2 = winner_kill2.loc[winner_kill2['map'] == 'ERANGEL']
miramar_kill2 = winner_kill2.loc[winner_kill2['map'] == 'MIRAMAR']
erangel_kill2 = erangel_kill2[['killer_position_x','killer_position_y']].value_counts()
miramar_kill2 = miramar_kill2[['killer_position_x','killer_position_y']].value_counts()

#kill3
winner_kill3 = kill_match_stats_final_3[['map','killer_position_x','killer_position_y']]
winner_kill3['killer_position_x'] = winner_kill3['killer_position_x'].div(1000).round(decimals=0)
winner_kill3['killer_position_y'] = winner_kill3['killer_position_y'].div(1000).round(decimals=0)
erangel_kill3 = winner_kill3.loc[winner_kill3['map'] == 'ERANGEL']
miramar_kill3 = winner_kill3.loc[winner_kill3['map'] == 'MIRAMAR']
erangel_kill3 = erangel_kill3[['killer_position_x','killer_position_y']].value_counts()
miramar_kill3 = miramar_kill3[['killer_position_x','killer_position_y']].value_counts()

#kill4
winner_kill4 = kill_match_stats_final_4[['map','killer_position_x','killer_position_y']]
winner_kill4['killer_position_x'] = winner_kill4['killer_position_x'].div(1000).round(decimals=0)
winner_kill4['killer_position_y'] = winner_kill4['killer_position_y'].div(1000).round(decimals=0)
erangel_kill4 = winner_kill4.loc[winner_kill4['map'] == 'ERANGEL']
miramar_kill4 = winner_kill4.loc[winner_kill4['map'] == 'MIRAMAR']
erangel_kill4 = erangel_kill4[['killer_position_x','killer_position_y']].value_counts()
miramar_kill4 = miramar_kill4[['killer_position_x','killer_position_y']].value_counts()

erangel_kill = pd.concat([erangel_kill1, erangel_kill2, erangel_kill3, erangel_kill4])
miramar_kill = pd.concat([miramar_kill1, miramar_kill2, miramar_kill3, miramar_kill4])

head_erangel_kill = erangel_kill.head(100)

# erangel_kill.to_csv(r'D:/amy/data vis/project/erangel_winner_kill.csv')
# miramar_kill.to_csv(r'D:/amy/data vis/project/miramar_winner_kill.csv')




##gun used for killing###

head_kill_match_stats_final_0 = kill_match_stats_final_0.head()
gun0 = kill_match_stats_final_0['killed_by'].value_counts()
gun1 = kill_match_stats_final_1['killed_by'].value_counts()
gun2 = kill_match_stats_final_2['killed_by'].value_counts()
gun3 = kill_match_stats_final_3['killed_by'].value_counts()
gun4 = kill_match_stats_final_4['killed_by'].value_counts()
gun = pd.concat([gun0,gun1,gun2,gun3,gun4])

# gun.to_csv(r'D:/amy/data vis/project/gun.csv')




##gun for winner###
winner_gun0 = winner_kill0['killed_by'].value_counts()
winner_gun1 = winner_kill1['killed_by'].value_counts()
winner_gun2 = winner_kill2['killed_by'].value_counts()
winner_gun3 = winner_kill3['killed_by'].value_counts()
winner_gun4 = winner_kill4['killed_by'].value_counts()
winner_gun = pd.concat([winner_gun0,winner_gun1,winner_gun2,winner_gun3,winner_gun4])

# # winner_gun.to_csv(r'D:/amy/data vis/project/winner_gun.csv')
