import pandas as pd
import plotly.graph_objects as go
import streamlit as st
from plotly.subplots import make_subplots

from plotly.subplots import make_subplots


def get_fig(pos_selected=None):
    # Read the datasets
    if pos_selected is None:
        pos_selected = ['Centers', 'PowerForwards', 'SmallForwards', 'ShootingGuards', 'PointGuards']
    season_stats_df = pd.read_csv('Seasons_Stats.csv')
    player_df = pd.read_csv('Players.csv')

    # Join the datasets on the "Player" field
    df = pd.merge(season_stats_df, player_df, on='Player')
    years = {"1950s": [1950, 1959],
             "1960s": [1960, 1969],
             "1970s": [1970, 1979],
             "1980s": [1980, 1989],
             "1990s": [1990, 1999],
             "2000s": [2000, 2009],
             "2010s": [2010, 2019]}

    # Filter the data for the specified decade
    trace_locations = [(1, 1), (1, 2), (2, 1), (2, 2), (3, 1), (3, 2), (3, 2)]

    fig_list = []
    i = 0
    for year in years.keys():
        merged_df = df[(df['Year'] >= years[year][0]) & (df['Year'] <= years[year][1])]
        # Create a scatter plot

        fig = go.Figure()

        if ("Centers" in pos_selected):
            # Add scatter trace for Centers
            centers_data = merged_df[merged_df['Pos'] == 'C']

            fig.add_trace(go.Scatter(
                x=centers_data['height'],
                y=centers_data['weight'],
                mode='markers',
                name='Centers',
                marker=dict(color='blue'), legendgroup=f"{i}",
                text=centers_data['Player']
            ))

        if ("PowerForwards" in pos_selected):
            # Add scatter trace for Centers
            centers_data = merged_df[merged_df['Pos'] == 'PF']

            fig.add_trace(go.Scatter(
                x=centers_data['height'],
                y=centers_data['weight'],
                mode='markers',
                name='PowerForwards',
                marker=dict(color='red'), legendgroup=f"{i}",
                text=centers_data['Player']
            ))

        if ("SmallForwards" in pos_selected):
            # Add scatter trace for Centers
            centers_data = merged_df[merged_df['Pos'] == 'SF']
            fig.add_trace(go.Scatter(
                x=centers_data['height'],
                y=centers_data['weight'],
                mode='markers',
                name='SmallForwards',
                marker=dict(color='green'), legendgroup=f"{i}",
                text=centers_data['Player']
            ))
        if ("ShootingGuards" in pos_selected):
            # Add scatter trace for Centers
            centers_data = merged_df[merged_df['Pos'] == 'SG']
            fig.add_trace(go.Scatter(
                x=centers_data['height'],
                y=centers_data['weight'],
                mode='markers',
                name='ShootingGuards',
                marker=dict(color='purple'), legendgroup=f"{i}",
                text=centers_data['Player']

            ))

        if ("PointGuards" in pos_selected):
            # Add scatter trace for Centers
            centers_data = merged_df[merged_df['Pos'] == 'PG']
            fig.add_trace(go.Scatter(
                x=centers_data['height'],
                y=centers_data['weight'],
                mode='markers',
                name='PointGuards',
                marker=dict(color='orange'), legendgroup=f"{i}",
                text=centers_data['Player']

            ))

        fig.update_layout(
            title=f'Players Height vs Weight for  ({year})',
            xaxis_title='Height (cm)',
            yaxis_title='Weight (kg)',
            showlegend=False,

            legend=dict(
                x=1,
                y=1.0,
                bgcolor='white',
                bordercolor='black'
            ),
            plot_bgcolor='white',

        )

        fig_list.append(fig)
        i += 1
    # Create a list of your 7 Plotly Go figures
    figures = fig_list[1:]

    # Create a new plot with subplots
    fig = make_subplots(rows=2, cols=3, subplot_titles=list(years.keys())[1:])

    # Iterate over the figures and add them to the subplots
    for i, fig_trace in enumerate(figures):
        row = i // 3 + 1
        col = i % 3 + 1
        for trace in fig_trace['data']:
            fig.add_trace(trace, row=row, col=col)
            fig.update_layout(
                title=f'Players Height vs Weight for  ({year})',
                xaxis_title='Height (cm)',
                yaxis_title='Weight (kg)',

                legend=dict(
                    x=1,
                    y=1.0,
                    bgcolor='white',
                    bordercolor='black'
                ),
                plot_bgcolor='white'
            )

    # Update the layout of the subplots

    fig.update_layout(height=600, width=1000, title_text="Height VS weight ")
    for i in range(3):
        for j in range(4):
            fig.update_xaxes(title_text="Height", row=i, col=j)
            fig.update_yaxes(title_text="Weight", row=i, col=j)
    names = set()

    fig.for_each_trace(lambda trace1: trace1.update(showlegend=False) if (trace1.name in names) else names.add(trace1.name))
    fig.update_yaxes(range=[50, 150])
    fig.update_xaxes(range=[150, 240])

    return fig
