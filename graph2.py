import plotly.graph_objects as go
import plotly.subplots as sp
import pandas as pd

# Read the dataset
df = pd.read_csv('Seasons_Stats.csv')

# Filter the dataset for the years 2012-2017
df_filtered = df[(df['Year'] >= 2012) & (df['Year'] <= 2017)]

def get_fig(year=2012):
    # Filter the dataset for the given year
    df_year = df_filtered[df_filtered['Year'] == year]

    # Create new subplots
    fig = sp.make_subplots(rows=1, cols=3, subplot_titles=("2PA", "3PA", "Age"))

    # Add box plots for each column
    columns = ['2PA', '3PA', 'Age']
    colors = ['#1f77b4', '#ff7f0e', '#2ca02c']

    for i, column in enumerate(columns):
        fig.add_trace(go.Box(y=df_year[column], name=column, marker_color=colors[i]), row=1, col=i+1)

    # Update the layout
    fig.update_layout(title=f'Statistics for Center Position in the Year: {year}',
                      xaxis=dict(title='Features'),
                      yaxis=dict(title='Values'),
                      showlegend=True)



    return fig
