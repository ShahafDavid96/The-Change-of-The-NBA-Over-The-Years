import streamlit as st
import pandas as pd
import graph1
import graph2
import graph3
from PIL import Image
from plotly.subplots import make_subplots

# Set up Streamlit page configuration
st.set_page_config(layout="wide")

# Create the graphs
graph1_fig = graph1.get_fig3p()
graph1_2_fig = graph1.get_fig2p()

# Set up the app layout
st.title("The Change of The NBA Over The Years")
st.write("Welcome to our NBA Dashboard—an all-inclusive platform designed to meticulously analyze and dissect the dynamic evolution of the NBA throughout the years. With a multitude of comprehensive tools and visualizations at your fingertips, our purpose is to provide an in-depth exploration of the changes that have shaped the landscape of professional basketball. Delve into captivating statistics, unravel trends, empowering you to gain unparalleled insights into the rich history and ever-evolving nature of the NBA.")
# Player position and graph type selection
st.write("---")

pos, radio = st.columns(2)

with pos:
    # Allow user to select player positions
    pos_selection = st.multiselect(
        "Select player positions:",
        ['Centers', 'PowerForwards', 'SmallForwards', 'ShootingGuards', 'PointGuards']
    )

with radio:
    # Allow user to select 2PA or 3PA
    graph1_radio = st.selectbox(
        "Select 2PA or 3PA:",
        ('2 Point Attempt', '3 Point Attempt'),
        index=0
    )

# Set default positions if none are selected
if len(pos_selection) == 0:
    pos_selection = ['Centers', 'PowerForwards', 'SmallForwards', 'ShootingGuards', 'PointGuards']

# Get the selected graph based on radio button selection
if graph1_radio == '2 Point Attempt':
    selected_graph1 = graph1.get_fig2p(pos_selection)
elif graph1_radio == '3 Point Attempt':
    selected_graph1 = graph1.get_fig3p(pos_selection)
else:
    selected_graph1 = graph1.get_fig3p(pos_selection)
st.write("---")


st.write("The goal of these graphs is to provide an overview of the average number of two-point and three-point attempts per game over the years, categorized by different player positions in basketball.")
st.write("By analyzing these graphs, individuals can gain insights into the evolving playing styles and shooting preferences of different positions throughout the years.")
# Display the selected graph
st.plotly_chart(selected_graph1, use_container_width=True)
st.write("---")


# Display graph3
st.write("The faceting graph allows for a comprehensive analysis of the relationship between height and weight across different decades for various player positions in basketball. By utilizing this visualization, one can observe how the average height and weight of players have evolved over time for different positions. The graph provides separate panels for each decade, allowing for easy comparison and identification of trends. It enables users to examine the distribution and variations in height and weight within each position, highlighting potential changes in player physique and position requirements.")
graph3_fig = graph3.get_fig(pos_selection)
st.plotly_chart(graph3_fig, use_container_width=True)

# Team selection
col1, col2, col3 = st.columns(3)
team_names = [
    'Atlanta Hawks', 'Boston Celtics', 'Brooklyn Nets', 'Charlotte Hornets', 'Chicago Bulls',
    'Cleveland Cavaliers', 'Dallas Mavericks', 'Denver Nuggets', 'Detroit Pistons',
    'Golden State Warriors', 'Houston Rockets', 'Indiana Pacers', 'Los Angeles Clippers',
    'Los Angeles Lakers', 'Memphis Grizzlies', 'Miami Heat', 'Milwaukee Bucks',
    'Minnesota Timberwolves', 'New Orleans Pelicans', 'New York Knicks',
    'Oklahoma City Thunder', 'Orlando Magic', 'Philadelphia 76ers', 'Phoenix Suns',
    'Portland Trail Blazers', 'Sacramento Kings', 'San Antonio Spurs', 'Toronto Raptors',
    'Utah Jazz', 'Washington Wizards'
]
st.write("---")
st.write("These graphs allow you to compare two teams based on their offensive and defensive performance in various aspects of the game. The offensive features include offensive rebounds (ORB), free throws made (FT), and assists (AST). These metrics reflect a team's ability to secure second-chance opportunities, convert free throws, and facilitate scoring through passing. On the other hand, the defensive features consist of steals (STL), blocks (BLK), and defensive rebounds (DRB). These metrics measure a team's ability to disrupt opponents' possessions, protect the rim, and secure defensive rebounds. By analyzing these features, you can gain insights into the strengths and weaknesses of teams' offensive and defensive playstyles.")
with col1:
    # Allow user to select Team1
    team1_select = st.selectbox("Select Team1", team_names, index=0)

with col2:
    # Allow user to select Play Style
    PS_selection = st.selectbox("Select Play Style:", ["Offensive", "Defensive"], index=0)

with col3:
    # Allow user to select Team2
    team2_select = st.selectbox("Select Team2", team_names, index=1)

# Display graph2 for Team1 and Team2
team1, team2 = st.columns(2)

with team1:
    st.plotly_chart(graph2.get_fig(team1_select, PS_selection), use_container_width=True)

with team2:
    st.plotly_chart(graph2.get_fig(team2_select, PS_selection), use_container_width=True)
