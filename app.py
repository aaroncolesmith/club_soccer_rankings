import pandas as pd
import streamlit as st
import plotly_express

df=pd.read_csv('aaroncolesmith/club_soccer_rankings/club_soccer_rankings.csv')

st.title('FiveThirtyEight Global Club Soccer Rankings Over Time')
st.markdown('[Data Credit: FiveThirtyEight Global Club Soccer Rankings](https://projects.fivethirtyeight.com/soccer-predictions/global-club-rankings/)')

px.scatter(df,
    x='date',
    y='rating',
    color='team')
