import streamlit as st
import pandas as pd
import plotly.express as px
import seaborn as sns
import matplotlib.pyplot as plt

df = pd.read_csv('ODI_Match_info.csv')
df_clean = df.dropna(subset=['toss_winner', 'winner'])

st.title("ODI Match Toss & Win Analysis")

st.subheader("Toss Wins by Each Team")
toss_win_counts = df_clean['toss_winner'].value_counts().reset_index()
toss_win_counts.columns = ['Team', 'Toss Wins']
fig_bar = px.bar(toss_win_counts, x='Team', y='Toss Wins', title="Toss Wins by Teams")
st.plotly_chart(fig_bar)

st.subheader("Toss Winning & Match Winning")
toss_match_win = df_clean[df_clean['toss_winner'] == df_clean['winner']]
toss_match_win_counts = toss_match_win['toss_winner'].value_counts().reset_index()
toss_match_win_counts.columns = ['Team', 'Wins After Toss Win']
fig_bar2 = px.bar(toss_match_win_counts, x='Team', y='Wins After Toss Win', title="Teams Winning Toss & Match")
st.plotly_chart(fig_bar2)

st.subheader("Toss Loser & Match Winner")
toss_loser_match_win = df_clean[df_clean['toss_winner'] != df_clean['winner']]
toss_loser_match_win_counts = toss_loser_match_win['winner'].value_counts().reset_index()
toss_loser_match_win_counts.columns = ['Team', 'Wins After Toss Loss']
fig_bar3 = px.bar(toss_loser_match_win_counts, x='Team', y='Wins After Toss Loss', title="Teams Losing Toss but Winning Match")
st.plotly_chart(fig_bar3)

st.subheader("Winning percentage by every Country")
total_matches = pd.concat([df_clean["team1"], df_clean["team2"]]).value_counts()
matches_win = df_clean['winner'].value_counts()
win_percentage = (matches_win/total_matches)*100
win_percentage = win_percentage.reset_index()
win_percentage.columns = ['Team', 'Win Percentage']
fig_pie = px.pie(win_percentage, values='Win Percentage', names='Team', title='Winning percentage by Team')
st.plotly_chart(fig_pie)
st.subheader('Toss decision by Teams')
toss_decision_counts = df_clean.groupby('toss_winner')['toss_decision'].value_counts().reset_index(name='count')
fig_toss_decision = px.bar(toss_decision_counts, x='toss_winner',y='count',color='toss_decision', barmode='group', title='Toss decision by Teams')
st.plotly_chart(fig_toss_decision)

st.subheader('Matches per Venue')
plt.figure(figsize=(10,6))
sns.countplot(y='venue', data=df_clean, order=df_clean['venue'].value_counts().index)
plt.title('Number of Matches per Venue')
st.pyplot(plt)