import streamlit as st 
from monty_hall import simulate_games
import time


st.title(":goat: Monty  Hall Simulation :game_die:")
st.write("")
st.image("image/images.png", width=500)

#? Input for num_games
num_games = st.number_input("Enter the number of games to simulate:", min_value=1, max_value = 100000,value=100)

col1, col2 = st.columns(2)

col1.subheader("Switching Strategy")
col2.subheader("Staying Strategy")

#! Initialize the charts for displaying win rates
chart1 = col1.line_chart(x= None, y = None, height=500,width=500)
chart2 = col2.line_chart(x= None, y = None, height=500,width=500)

wins_switching = 0
wins_without_switching = 0

for i in range(num_games):
    """
    Simulate a single game of Monty Hall and update the charts with the current win rates.
    This loop runs for the number of games specified by the user.
    """
    num_wins_without_switching, num_wins_with_switching = simulate_games(num_games=1)
    wins_switching += num_wins_with_switching
    wins_without_switching += num_wins_without_switching
    
    chart1.add_rows([wins_switching / (i + 1)])
    chart2.add_rows([wins_without_switching / (i + 1)])
    
    time.sleep(0.01)  # Adding a small delay to visualize the chart update

    