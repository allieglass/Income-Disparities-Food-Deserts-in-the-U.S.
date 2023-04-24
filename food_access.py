import streamlit as st
import pandas as pd
import geopandas as gpd
import altair as alt
import numpy as np
import matplotlib.pyplot as plt
import zipfile

@st.cache_data
def load_data():
    zf = zipfile.ZipFile('foodaccessdata2019.csv.zip')
    food_data = pd.read_csv(zf.open('foodaccessdata2019.csv'))
    food_data.dropna(subset=['PovertyRate'], inplace=True)
    return food_data

food_data = load_data()

st.header("**Income Disparities & Food Deserts in the U.S.**")

st.markdown("Food Deserts are geographical locations where low-income communities do not have access to a store with affordable fresh foods.")

tab1, tab2 = st.tabs(["Poverty Rates in the U.S.","Food Deserts in the U.S."])

with tab1:
    num_states = st.slider('Number of states to display:', 1, len(food_data['State'].unique()), 10)

    n_by_state = food_data.groupby('State')['PovertyRate'].mean().reset_index()

    sorted_states = n_by_state.sort_values(by='PovertyRate', ascending=False)
    top_states = sorted_states['State'].head(num_states).tolist()

    top_data = food_data[food_data['State'].isin(top_states)]

    chart = alt.Chart(top_data).mark_bar(color='orange').encode(
        x='State:N',
        y=alt.Y('PovertyRate:Q', axis=alt.Axis(title='Average Poverty Rate', labels=False)),
        tooltip=[alt.Tooltip('State:N'), alt.Tooltip('PovertyRate:Q')]
    ).properties(
        width=600,
        height=600,
        title=f'Top {num_states} states with highest Poverty Rate'
    )
    st.altair_chart(chart, use_container_width=True)

with tab2: 
    selected_state = st.selectbox('Select state', food_data['State'].unique())

    state_data = food_data[food_data['State'] == selected_state]

    sum_by_state_white = state_data['lawhite10'].sum()
    sum_by_state_black = state_data['lablack10'].sum()
    sum_by_state_hisp = state_data['lahisp10'].sum()
    sum_by_state_asian = state_data['laasian10'].sum()
    
    labels = ['White','Black','Hispanic','Asian']
    values = [sum_by_state_white, sum_by_state_black, sum_by_state_hisp, sum_by_state_asian]

    fig, ax = plt.subplots()
    ax.bar(labels, values, color='orange')
    ax.set_xlabel('Ethnicity')
    ax.set_ylabel('  ')
    ax.set_title('Ethnicities 10-miles from a grocery store in {}'.format(selected_state))

    st.pyplot(fig)
