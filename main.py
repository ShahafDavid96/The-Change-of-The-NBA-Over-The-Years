import streamlit as st
import plotly.express as px
import pandas as pd
import graph1
import graph2
import graph3
# Generate example data
df3 = px.data.tips()
df4 = px.data.gapminder().query("year == 2007")
df5 = pd.DataFrame({'fruits': ['Apple', 'Orange', 'Banana'], 'counts': [20, 14, 35]})

# Create the graphs
graph1_fig = graph1.get_fig3p()
graph1_2_fig = graph1.get_fig2p()
graph2_fig = graph2.get_fig()
graph3_fig = px.scatter(df3, x='total_bill', y='tip', color='sex')
graph4_fig = px.scatter(df4, x='gdpPercap', y='lifeExp', size='pop', color='continent', log_x=True)
graph5_fig = px.pie(df5, values='counts', names='fruits')

# Set up the app layout
st.title("The Change of The NBA Over The Years")
graph1_radio = st.selectbox(
    "Select 2PA or 3PA:",
    ('2PA', '3PA'),
    index=0
)
graph1_selection = st.multiselect(
    "Select player positions :",
    ['Centers', 'PowerForwards', 'SmallForwards', 'ShootingGuards', 'PointGuards']
)
if len(graph1_selection)==0:
    graph1_selection=['Centers', 'PowerForwards', 'SmallForwards', 'ShootingGuards', 'PointGuards']
if graph1_radio == '2PA':
    selected_graph1 = graph1.get_fig2p(graph1_selection)
elif graph1_radio == '3PA':
    selected_graph1 = graph1.get_fig3p(graph1_selection)
else:
    selected_graph1 = graph1.get_fig3p(graph1_selection)


# Plot the graphs
st.plotly_chart(selected_graph1)

graph2_selection = st.selectbox(
    "Select Decade:",
    ["1950s", "1960s","1970s","1980s","1990s","2000s","2010s"],
    index=0
)

graph2_fig=graph2.get_fig(graph2_selection)
#st.plotly_chart(graph2_fig)
graph3_fig=graph3.get_fig(graph2_selection,graph1_selection)
st.plotly_chart(graph3_fig)
st.plotly_chart(graph4_fig)
st.plotly_chart(graph5_fig)
