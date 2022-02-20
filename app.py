import pandas as pd
import streamlit as st
import plotly_express as px

df = pd.read_csv("club_soccer_rankings.csv")

st.title("FiveThirtyEight Global Club Soccer Rankings Over Time")

fig = px.line(df, x="date", y="rating", color="team", render_mode="svg", mode="lines",line_shape="spline")

st.plotly_chart(fig, use_container_width=True)

st.markdown(
    "[Data Credit: FiveThirtyEight Global Club Soccer Rankings](https://projects.fivethirtyeight.com/soccer-predictions/global-club-rankings/)"
)
