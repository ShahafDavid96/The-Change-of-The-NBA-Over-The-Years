import plotly.graph_objects as go
import pandas as pd

# Read the dataset
df = pd.read_csv('Seasons_Stats.csv')
df= df.loc[df['Year'] > 1979]
nba_teams = {
    'Atlanta Hawks': ['Tri-Cities Blackhawks', 'Milwaukee Hawks', 'St. Louis Hawks'],
    'Boston Celtics': [],
    'Brooklyn Nets': ['New Jersey Nets'],
    'Charlotte Hornets': ['Charlotte Bobcats'],
    'Chicago Bulls': [],
    'Cleveland Cavaliers': [],
    'Dallas Mavericks': [],
    'Denver Nuggets': [],
    'Detroit Pistons': [],
    'Golden State Warriors': ['San Francisco Warriors', 'Philadelphia Warriors'],
    'Houston Rockets': ['San Diego Rockets'],
    'Indiana Pacers': [],
    'Los Angeles Clippers': ['San Diego Clippers'],
    'Los Angeles Lakers': ['Minneapolis Lakers'],
    'Memphis Grizzlies': ['Vancouver Grizzlies'],
    'Miami Heat': [],
    'Milwaukee Bucks': [],
    'Minnesota Timberwolves': [],
    'New Orleans Pelicans': ['New Orleans Hornets', 'New Orleans/Oklahoma City Hornets', 'Charlotte Hornets'],
    'New York Knicks': [],
    'Oklahoma City Thunder': ['Seattle SuperSonics'],
    'Orlando Magic': [],
    'Philadelphia 76ers': ['Syracuse Nationals'],
    'Phoenix Suns': [],
    'Portland Trail Blazers': [],
    'Sacramento Kings': ['Kansas City Kings', 'Kansas City-Omaha Kings', 'Cincinnati Royals', 'Rochester Royals'],
    'San Antonio Spurs': [],
    'Toronto Raptors': [],
    'Utah Jazz': ['New Orleans Jazz'],
    'Washington Wizards': ['Washington Bullets', 'Capital Bullets', 'Baltimore Bullets', 'Chicago Zephyrs',
                           'Chicago Packers']
}
all_colors = {
    "ORB": "#e41a1c",   # Red
    "FT": "#377eb8",    # Blue
    "AST": "#4daf4a",   # Green
    "STL": "#984ea3",   # Purple
    "BLK": "#ff7f00",   # Orange
    "DRB": "#b3b3cc"    # Yellow
}

names = {
    "ORB": "Offensive Rebound",
    "FT": "Free Throw",
    "AST": "Assists",
    "STL": "Steals",
    "BLK": "Blocks",
    "DRB": "Defensive Rebounds"
}
def get_fig(Tm, ps):
    feature=[]

    team_dict = {
        'Fort Wayne Pistons': 'FTW',
        'Indianapolis Olympians': 'INO',
        'Chicago Stags': 'CHS',
        'Toronto Huskies': 'TOT',
        'Denver Nuggets': 'DEN',
        'New York Knicks': 'NYK',
        'Tri-Cities Blackhawks': 'TRI',
        'Anderson Packers': 'AND',
        'Philadelphia Warriors': 'PHW',
        'Waterloo Hawks': 'WAT',
        'Sheboygan Red Skins': 'SHE',
        'Rochester Royals': 'ROC',
        'Baltimore Bullets': 'BLB',
        'Minneapolis Lakers': 'MNL',
        'Syracuse Nationals': 'SYR',
        'Washington Capitols': 'WSC',
        'Boston Celtics': 'BOS',
        'St. Louis Bombers': 'STB',
        'Milwaukee Hawks': 'MLH',
        'St. Louis Hawks': 'STL',
        'Detroit Pistons': 'DET',
        'Cincinnati Royals': 'CIN',
        'Los Angeles Lakers': 'LAL',
        'Chicago Packers': 'CHP',
        'San Francisco Warriors': 'SFW',
        'Chicago Zephyrs': 'CHZ',
        'Baltimore Bullets': 'BAL',
        'Philadelphia 76ers': 'PHI',
        'Chicago Bulls': 'CHI',
        'San Diego Rockets': 'SDR',
        'Seattle SuperSonics': 'SEA',
        'Milwaukee Bucks': 'MIL',
        'Atlanta Hawks': 'ATL',
        'Phoenix Suns': 'PHO',
        'Portland Trail Blazers': 'POR',
        'Cleveland Cavaliers': 'CLE',
        'Buffalo Braves': 'BUF',
        'Houston Rockets': 'HOU',
        'Golden State Warriors': 'GSW',
        'Kansas City-Omaha Kings': 'KCO',
        'Capital Bullets': 'CAP',
        'New Orleans Jazz': 'NOJ',
        'Washington Bullets': 'WSB',
        'Kansas City Kings': 'KCK',
        'Indiana Pacers': 'IND',
        'New York Nets': 'NYN',
        'San Antonio Spurs': 'SAS',
        'New Jersey Nets': 'NJN',
        'San Diego Clippers': 'SDC',
        'Utah Jazz': 'UTA',
        'Dallas Mavericks': 'DAL',
        'Los Angeles Clippers': 'LAC',
        'Sacramento Kings': 'SAC',
        'Charlotte Hornets': 'CHH',
        'Miami Heat': 'MIA',
        'Orlando Magic': 'ORL',
        'Minnesota Timberwolves': 'MIN',
        'Vancouver Grizzlies': 'VAN',
        'Toronto Raptors': 'TOR',
        'Washington Wizards': 'WAS',
        'Memphis Grizzlies': 'MEM',
        'New Orleans Hornets': 'NOH',
        'Charlotte Bobcats': 'CHA',
        'New Orleans/Oklahoma City Hornets': 'NOK',
        'Oklahoma City Thunder': 'OKC',
        'Brooklyn Nets': 'BRK',
        'New Orleans Pelicans': 'NOP',
        'Charlotte Hornets': 'CHO'
    }
    options=[Tm]+nba_teams[Tm]

    options=[team_dict[x] for x in options]

    filtered_df = df[df['Tm'].isin(options)]

    filtered_df.loc[:, 'Tm'] =team_dict[Tm]
    filtered_df=filtered_df.fillna(0)
    # Group the DataFrame by 'Year'
    grouped = filtered_df.groupby('Year')

    # Create the plot
    feature_plots=[]

        # Determine the features based on the option
    if ps == "Offensive":
            features = [ "ORB", "FT", "AST"]
    else:
            features = ["STL", "BLK", "DRB"]

        # Iterate over the features
    for feature in features:
            # Get the data for the current feature
            data = grouped[feature].mean()

            # Create a scatter plot for the feature
            feature_plots.append(go.Scatter(x=data.index, y=data.values, name=names[feature],marker=dict(color=all_colors[feature])))


    # Set the layout
    layout=go.Layout(
    title=f'Stats for {ps} Play Style for {Tm}',
    xaxis=dict(
        title='Years',
        titlefont=dict(size=16, color='#000000'),
        tickfont=dict(size=14, color='#000000')
    ),
    yaxis=dict(
        title='Mean of The Feature',
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
    fig = go.Figure(data=feature_plots, layout=layout)

    # Show the plot
    return fig

