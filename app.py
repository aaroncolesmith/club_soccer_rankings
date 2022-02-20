import pandas as pd
import streamlit as st
import plotly_express as px

df=pd.read_csv('club_soccer_rankings.csv')

st.title('FiveThirtyEight Global Club Soccer Rankings Over Time')
st.markdown('[Data Credit: FiveThirtyEight Global Club Soccer Rankings](https://projects.fivethirtyeight.com/soccer-predictions/global-club-rankings/)')

fig=px.scatter(df,
    x='date',
    y='rating',
    color='team')
st.plotly_chart(fig, use_container_width=True)
