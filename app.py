import pandas as pd
import streamlit as st
import plotly_express as px

df = pd.read_csv("club_soccer_rankings.csv")

st.title("FiveThirtyEight Global Club Soccer Rankings Over Time")
st.markdown(
    "[Data Credit: FiveThirtyEight Global Club Soccer Rankings](https://projects.fivethirtyeight.com/soccer-predictions/global-club-rankings/)"
)

fig = px.line(df, x="date", y="rating", color="team", render_mode="svg")
fig.update_traces(
    mode="lines",
    line_shape="spline",
    opacity=0.75,
    marker=dict(size=8, line=dict(width=1, color="DarkSlateGrey")),
    line=dict(width=4),
)
st.plotly_chart(fig, use_container_width=True)


