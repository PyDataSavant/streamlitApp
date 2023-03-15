import pandas as pd
import streamlit as st

# !pip install matplotlib
import matplotlib.pyplot as plt

# !pip install plotly
# import plotly.graph_objects as go
import plotly.express as px


df1 = pd.read_csv('complete_user_story_info.csv')
df2 = pd.read_csv('sprint_wise_story_info.csv')

st.sidebar.title('User Story Analysis')

option = st.sidebar.selectbox('Select Any One', ['Top Scorer', 'Group Bar Plot', 'Highest Sprint grosser'])

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
    st.sidebar.selectbox('Select individual', ['Show Stacked Bar Plot'])
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

# 3.Finding Individuals with Highest Story Points in a Single Sprint.
elif option == 'Highest Sprint grosser':
    st.sidebar.selectbox('Select individual', ['bar plot using plotly.express'])
    btn3 = st.sidebar.button('Find Details')
    if btn3:
        st.title('Finding Individuals with Highest Story Points in a Single Sprint')
        max_rs = df2[df2['name'] == 'RS']['story_points'].max()
        max_pd = df2[df2['name'] == 'PD']['story_points'].max()
        max_jp = df2[df2['name'] == 'JP']['story_points'].max()

        rs_df = df2[df2['story_points'] == max_rs]
        pd_df = df2[df2['story_points'] == max_pd]
        jp_df = df2[df2['story_points'] == max_jp]

        sprint_max = rs_df.append(pd_df, ignore_index=True).append(jp_df, ignore_index=True)

        st.write('Bar Chart')
        st.bar_chart(sprint_max, x='name', y=['story_points', 'name'], use_container_width=True)

        st.write('Data Analysis')
        st.write(sprint_max)