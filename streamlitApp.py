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

option = st.sidebar.selectbox('Select Any One', ['Top Scorer', 'Group Bar Plot', 'Highest Sprint grosser',
                                                 'Top 2 Story', 'Tech-Func Story Expert',
                                                 'Alert-Monitoring Story Expert', 'sum_of_storypoints_title_wise'])

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

# 4.Show top 2 highest story points for story title for all individuals
elif option == 'Top 2 Story':
    st.sidebar.selectbox('Select individual', ['Showing Top 2 Story'])
    btn4 = st.sidebar.button('Find Details')
    if btn4:
        st.title('Show top 2 highest story points for story title for all individuals')
        top2_rs_df = df1[df1['name'] == 'RS'].groupby(['name', 'story_name'])['story_points'].sum().sort_values(
            ascending=False).reset_index().head(2)
        top2_pd_df = df1[df1['name'] == 'PD'].groupby(['name', 'story_name'])['story_points'].sum().sort_values(
            ascending=False).reset_index().head(2)
        top2_jp_df = df1[df1['name'] == 'JP'].groupby(['name', 'story_name'])['story_points'].sum().sort_values(
            ascending=False).reset_index().head(2)

        top2_story_name = top2_rs_df.append(top2_pd_df, ignore_index=True).append(top2_jp_df, ignore_index=True)

        st.write('Bar Chart')
        st.bar_chart(top2_story_name, x='name', y='story_points', use_container_width=True)
        st.write('Maximum Story Points Obtained in top 2 story')
        st.write(top2_story_name)

# 5.Show maximum story points in Tech and func spec for all individuals
elif option == 'Tech-Func Story Expert':
    st.sidebar.selectbox('Select individual', ['Sum of Tech_cum_Func_Spec'])
    btn5 = st.sidebar.button('Find Details')
    if btn5:
        st.title('Show maximum story points in Tech and func spec for all individuals')

        tech_df = df1[df1['story_name'] == 'Tech Spec'].groupby(['name', 'story_name'])[
            'story_points'].sum().reset_index().sort_values(by='story_points', ascending=False)
        func_df = df1[df1['story_name'] == 'Functional'].groupby(['name', 'story_name'])[
            'story_points'].sum().reset_index().sort_values(by='story_points', ascending=False)

        tech_func_df = tech_df.append(func_df, ignore_index=True).groupby('name')[
            'story_points'].sum().reset_index().sort_values(by='story_points', ascending=False)

        st.write('Data Vizualized')
        fig1, ax1 = plt.subplots()
        ax1.pie(tech_func_df['story_points'], labels=tech_func_df['name'], autopct='%1.1f%%',
                shadow=True, startangle=90)
        ax1.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.

        st.pyplot(fig1)

        st.write('Showing dataframe')
        st.write(tech_func_df)

# 6.Show maximum story points for alerting and Monitoring
elif option == 'Alert-Monitoring Story Expert':
    st.sidebar.selectbox('Select individual', ['Sum of Alerting_cum_Monitoring_Story'])
    btn6 = st.sidebar.button('Find Details')
    if btn6:
        st.title('Show maximum story points for alerting and Monitoring')

        alert_df = df1[df1['story_name'] == 'Alerting'].groupby(['name', 'story_name'])[
            'story_points'].sum().reset_index().sort_values(by='story_points', ascending=False)
        monitor_df = df1[df1['story_name'] == 'Monitoring'].groupby(['name', 'story_name'])[
            'story_points'].sum().reset_index().sort_values(by='story_points', ascending=False)

        alert_monitor_df = alert_df.append(monitor_df, ignore_index=True).groupby('name')[
            'story_points'].sum().reset_index().sort_values(by='story_points', ascending=False)

        st.write('Data Vizualized')
        fig1, ax1 = plt.subplots()
        ax1.pie(alert_monitor_df['story_points'], labels=alert_monitor_df['name'], autopct='%1.1f%%',
                shadow=True, startangle=90)
        ax1.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.

        st.pyplot(fig1)

        st.write('Showing dataframe')
        st.write(alert_monitor_df)

# 7.Show all story points in all story title for all individuals
elif option == 'sum_of_storypoints_title_wise':
    st.sidebar.selectbox('Select individual', ['Sum of score story wise'])
    btn7 = st.sidebar.button('Find Details')
    if btn7:
        st.title('Show all story points in all story title for all individuals')
        sum_of_storypoints_title_wise = df1[['name', 'story_name', 'story_points']].groupby(['name', 'story_name'])[
            'story_points'].sum()

        temp_df = sum_of_storypoints_title_wise.reset_index()
        st.write('Vizualized Data')
        st.plotly_chart(px.bar(temp_df, x='story_name', y='story_points', color='name'))

        st.write('Aggregate story points for all individuals')
        st.write(sum_of_storypoints_title_wise)

