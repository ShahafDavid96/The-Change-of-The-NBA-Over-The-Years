import streamlit as st
import plotly.express as px
import pandas as pd
import graph1
import graph2
import graph3
from PIL import Image


from plotly.subplots import make_subplots
st.set_page_config(layout="wide")
# Generate example data
df3 = px.data.tips()
df4 = px.data.gapminder().query("year == 2007")
df5 = pd.DataFrame({'fruits': ['Apple', 'Orange', 'Banana'], 'counts': [20, 14, 35]})

# Create the graphs
graph1_fig = graph1.get_fig3p()
graph1_2_fig = graph1.get_fig2p()
graph3_fig = px.scatter(df3, x='total_bill', y='tip', color='sex')
graph4_fig = px.scatter(df4, x='gdpPercap', y='lifeExp', size='pop', color='continent', log_x=True)
graph5_fig = px.pie(df5, values='counts', names='fruits')

# Set up the app layout
st.title("The Change of The NBA Over The Years")

pos,radio= st.columns(2)
with pos:
    pos_selection = st.multiselect(
            "Select player positions :",
            ['Centers', 'PowerForwards', 'SmallForwards', 'ShootingGuards', 'PointGuards']
        )

with radio:
    graph1_radio = st.selectbox(
        "Select 2PA or 3PA:",
        ('2PA', '3PA'),
        index=0
    )

if len(pos_selection)==0:
    pos_selection=['Centers', 'PowerForwards', 'SmallForwards', 'ShootingGuards', 'PointGuards']
if graph1_radio == '2PA':
    selected_graph1 = graph1.get_fig2p(pos_selection)
elif graph1_radio == '3PA':
    selected_graph1 = graph1.get_fig3p(pos_selection)
else:
    selected_graph1 = graph1.get_fig3p(pos_selection)


st.plotly_chart(selected_graph1,use_container_width=True)



graph3_fig=graph3.get_fig(pos_selection)
st.plotly_chart(graph3_fig,use_container_width=True)
col1,col2,col3=st.columns(3)
team_names = ['Atlanta Hawks', 'Boston Celtics', 'Brooklyn Nets', 'Charlotte Hornets', 'Chicago Bulls', 'Cleveland Cavaliers', 'Dallas Mavericks', 'Denver Nuggets', 'Detroit Pistons', 'Golden State Warriors', 'Houston Rockets', 'Indiana Pacers', 'Los Angeles Clippers', 'Los Angeles Lakers', 'Memphis Grizzlies', 'Miami Heat', 'Milwaukee Bucks', 'Minnesota Timberwolves', 'New Orleans Pelicans', 'New York Knicks', 'Oklahoma City Thunder', 'Orlando Magic', 'Philadelphia 76ers', 'Phoenix Suns', 'Portland Trail Blazers', 'Sacramento Kings', 'San Antonio Spurs', 'Toronto Raptors', 'Utah Jazz', 'Washington Wizards']
with col1:
    team1_select = st.selectbox(
            "Select Team1",
            team_names,
            index=0)
with col2:
    PS_selection = st.selectbox(
            "Select Play Style:",
            ["Offensive", "Defensive"],
            index=0)
with col3:
    team2_select = st.selectbox(
            "Select Team2",
            team_names,
            index=1)
team1,team2=st.columns(2)
with team1:
    st.plotly_chart(graph2.get_fig(team1_select,PS_selection),use_container_width=True)
with team2:
    st.plotly_chart(graph2.get_fig(team2_select,PS_selection),use_container_width=True)
