import numpy as np
import pandas as pd
import streamlit as st

# !pip install matplotlib
import matplotlib.pyplot as plt

# !pip install plotly
import plotly.graph_objects as go
import plotly.express as px


df1 = pd.read_csv('complete_user_story_info.csv')
df2 = pd.read_csv('sprint_wise_story_info.csv')

st.sidebar.title('User Story Analysis')

option = st.sidebar.selectbox('Select Any One', ['Top Scorer', 'Group Bar Plot'])

# 1. Top employee of 2022 : Total story points obtained by every individuals
if option == 'Top Scorer':
    btn1 = st.sidebar.button('Find Details')
    if btn1:
        st.title('Bar graph showing Total story points in 2022')
        temp_df = df1.groupby('name')['story_points'].sum().sort_values(ascending=False)
        fig, ax = plt.subplots()
        ax.bar(temp_df.index, temp_df.values)
        st.pyplot(fig)


# 2.Grouped Bar Plot Showing Story Points per Sprint for all task holders
elif option == 'Group Bar Plot':
    btn2 = st.sidebar.button('Find Details')
    if btn2:
        temp_df = df2[df2['name'].isin(['RS', 'PD', 'JP'])].pivot(index='sprint_id', columns='name',
                                                                  values='story_points')
        px.bar(temp_df, x=temp_df.index, y=temp_df.columns, barmode='group', log_y=True, text_auto=True)
        st.title('Grouped Bar Plot Showing Story Points per Sprint for all task holders')
        st.write('Stacked Bar Chart')
        st.bar_chart(temp_df)
        st.write('Total Story Points Obtained')
        st.write(temp_df)
