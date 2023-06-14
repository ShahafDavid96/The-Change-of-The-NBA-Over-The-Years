import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import plotly
import plotly.offline as pyo
import plotly.graph_objs as go
import plotly.io as pio
# Function to create 'xGame' column, to calculate the average for stats per game
# x == DataFrame ; y == Column

def pergame(x, y):
    x[y + 'xG'] = round(x[y]/x['G'], 2)

seasons_stats = pd.read_csv("Seasons_Stats.csv")

#Preprocess
seasons_stats = seasons_stats.fillna(0)  # Fille Nan with 0
seasons_stats = seasons_stats[seasons_stats.Tm != 'TOT']

#Extract relevant years
seasons_stats1980 = seasons_stats.loc[seasons_stats['Year'] > 1979]
seasons_stats3p = seasons_stats.loc[seasons_stats['Year'] > 1979]

seasons_stats3p = seasons_stats3p[['Year', 'Pos', 'Player', 'G', '2PA', '3PA', 'FGA']]

seasons_stats3p_years = seasons_stats3p.groupby('Year').sum()
totyears = seasons_stats3p_years.index

seasons_stats3p_game = seasons_stats[['Year', 'Pos', 'G', 'MP', '2PA', '3PA', 'FGA', 'eFG%']]

# filtered by player who played more than 24 games in a season
seasons_stats3p_game = seasons_stats3p_game.loc[(seasons_stats3p_game['Year'] > 1979) & (seasons_stats3p_game['G'] > 24)]

#MinutsxGame column and filter by  > 17 MPxG
pergame(seasons_stats3p_game, 'MP')

seasons_stats3p_game = seasons_stats3p_game.loc[seasons_stats3p_game['MPxG'] > 17]

#Attemps per game
pergame(seasons_stats3p_game, '2PA')
pergame(seasons_stats3p_game, '3PA')
pergame(seasons_stats3p_game, 'FGA')

numeric_columns = seasons_stats3p_game.select_dtypes(include=[int, float]).columns
seasons_stats3p_game['eFG%'] = round(seasons_stats3p_game['eFG%'] * 100, 2)
shots_game_c = round(seasons_stats3p_game[seasons_stats3p_game['Pos'] == 'C'].groupby('Year')[numeric_columns].mean(),2)
shots_game_pf = round(seasons_stats3p_game.loc[seasons_stats3p_game['Pos'] == 'PF'].groupby('Year')[numeric_columns].mean(),2)
shots_game_sf = round(seasons_stats3p_game.loc[seasons_stats3p_game['Pos'] == 'SF'].groupby('Year')[numeric_columns].mean(),2)
shots_game_sg = round(seasons_stats3p_game.loc[seasons_stats3p_game['Pos'] == 'SG'].groupby('Year')[numeric_columns].mean(),2)
shots_game_pg = round(seasons_stats3p_game.loc[seasons_stats3p_game['Pos'] == 'PG'].groupby('Year')[numeric_columns].mean(),2)
shots_game_gen = round(seasons_stats3p_game.groupby('Year')[numeric_columns].mean(),2)

years_shotsgame = shots_game_c.index

p3c = go.Scatter(x=years_shotsgame, y=shots_game_c['3PAxG'], name='Centers', marker=dict(color='blue'))
p3pf = go.Scatter(x=years_shotsgame, y=shots_game_pf['3PAxG'], name='PowerForwards', marker=dict(color='red'))
p3sf = go.Scatter(x=years_shotsgame, y=shots_game_sf['3PAxG'], name='SmallForwards', marker=dict(color='green'))
p3sg = go.Scatter(x=years_shotsgame, y=shots_game_sg['3PAxG'], name='ShootingGuards', marker=dict(color='purple'))
p3pg = go.Scatter(x=years_shotsgame, y=shots_game_pg['3PAxG'], name='PointGuards', marker=dict(color='orange'))
p3gen = go.Bar(x=years_shotsgame, y=shots_game_gen['3PAxG'], name='Average', marker=dict(color='#FFB3A7'))

data=[p3c,p3pf,p3sf,p3sg,p3pg,p3gen]
layout_3p=go.Layout(
    title='Mean 3P attempts per game by position',
    xaxis=dict(
        title='Years',
        titlefont=dict(size=16, color='#000000'),
        tickfont=dict(size=14, color='#000000'),
    ),
    yaxis=dict(
        title='Mean 3 points attempts per game',
        titlefont=dict(size=16, color='#000000'),
        tickfont=dict(size=14, color='#000000'),
        showgrid=True, gridwidth=0.2, gridcolor='#D7DBDD'
    ),
    legend=dict(
        x=1,
        y=1.0,
        bgcolor='white',
        bordercolor='black'
    ),
    plot_bgcolor='white',
    barmode='group',
    bargap=0.15,
    bargroupgap=0.1
)

fig_3p = go.Figure(data=data, layout=layout_3p)

p2c = go.Scatter(x=years_shotsgame, y=shots_game_c['2PAxG'], name='Centers', marker=dict(color='blue'))
p2pf = go.Scatter(x=years_shotsgame, y=shots_game_pf['2PAxG'], name='PowerForwards', marker=dict(color='red'))
p2sf = go.Scatter(x=years_shotsgame, y=shots_game_sf['2PAxG'], name='SmallForwards', marker=dict(color='green'))
p2sg = go.Scatter(x=years_shotsgame, y=shots_game_sg['2PAxG'], name='ShootingGuards', marker=dict(color='purple'))
p2pg = go.Scatter(x=years_shotsgame, y=shots_game_pg['2PAxG'], name='PointGuards', marker=dict(color='orange'))
p2gen = go.Bar(x=years_shotsgame, y=shots_game_gen['2PAxG'], name='Average', marker=dict(color='#FFB3A7'))

data=[p2c,p2pf,p2sf,p2sg,p2pg,p2gen]
layout_2p=go.Layout(
    title='Mean 2P attempts per game by position',
    xaxis=dict(
        title='Years',
        titlefont=dict(size=16, color='#000000'),
        tickfont=dict(size=14, color='#000000')
    ),
    yaxis=dict(
        title='Mean 2 points attempts per game',
        titlefont=dict(size=16, color='#000000'),
        tickfont=dict(size=14, color='#000000'),
        showgrid=True, gridwidth=0.2, gridcolor='#D7DBDD'
    ),
    legend=dict(
        x=1,
        y=1.0,
        bgcolor='white',
        bordercolor='black'
    ),
    plot_bgcolor='white',
    barmode='group',
    bargap=0.15,
    bargroupgap=0.1
)


fig_2p = go.Figure(data=data, layout=layout_2p)

def get_fig3p(data=None):
    if data is None:
        data = [p3c, p3pf, p3sf, p3sg, p3pg, p3gen]
        return go.Figure(data=data, layout=layout_3p)
    selected_data=[]

    for obj in data:
        if obj == 'Centers':
            selected_data.append(p3c)
        if obj == 'PowerForwards':
            selected_data.append(p3pf)
        if obj == 'SmallForwards':
            selected_data.append(p3sf)
        if obj == 'ShootingGuards':
            selected_data.append(p3sg)
        if obj == 'PointGuards':
            selected_data.append(p3pg)
    selected_data.append(p3gen)
    fig_3p = go.Figure(data=selected_data, layout=layout_3p)

    return fig_3p

def get_fig2p(data=None):
    if data is None:
        data=[p2c,p2pf,p2sf,p2sg,p2pg,p2gen]
        return go.Figure(data=data, layout=layout_2p)
    selected_data=[]

    for obj in data:
        if obj == 'Centers':
            selected_data.append(p2c)
        if obj == 'PowerForwards':
            selected_data.append(p2pf)
        if obj == 'SmallForwards':
            selected_data.append(p2sf)
        if obj == 'ShootingGuards':
            selected_data.append(p2sg)
        if obj == 'PointGuards':
            selected_data.append(p2pg)
    selected_data.append(p2gen)
    fig_2p = go.Figure(data=selected_data, layout=layout_2p)


    return fig_2p