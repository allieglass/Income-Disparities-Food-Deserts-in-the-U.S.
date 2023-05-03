import streamlit as st
import pandas as pd
import altair as alt
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

st.markdown("Food Deserts are geographical locations where low-income communities do not have access to a store with affordable fresh foods. Choose from the pages on the left to see which states and which ethnicities have more food deserts and worse poverty rates than others.")

page_options = ["Poverty Rates in the U.S.", "Ethnicities by State in Food Deserts"]
page = st.sidebar.selectbox("Choose from the options below:", page_options)

if "Poverty Rates in the U.S." in page:
    st.markdown("**Poverty Rates in the U.S.**")
    
    n_by_state = food_data[['State', 'PovertyRate']].groupby(['State']).mean().reset_index()

    chart = alt.Chart(n_by_state).mark_bar(color='orange').encode(
        x='State:N',
        y=alt.Y('PovertyRate:Q', axis=alt.Axis(title='Average Poverty Rate', labels=False)),
        tooltip=[alt.Tooltip('State:N'), alt.Tooltip('PovertyRate:Q')]
    ).properties(
        width=600,
        height=600,
    )
    st.altair_chart(chart, use_container_width=True)
    
if "Ethnicities by State in Food Deserts" in page:
    st.markdown("**Ethnicities by State in Food Deserts**")
    tab1, tab2, tab3= st.tabs(['1-mile from a grocery store', '10-miles from a grocery store', '20-miles from a grocery store'])

    with tab1:
        selected_state1 = st.selectbox('Select state', food_data['State'].unique(), key='tab1_selectbox')

        state_data1 = food_data[food_data['State'] == selected_state1]

        sum_by_state_white1 = state_data1['lawhite1'].sum()
        sum_by_state_black1 = state_data1['lablack1'].sum()
        sum_by_state_hisp1 = state_data1['lahisp1'].sum()
        sum_by_state_asian1 = state_data1['laasian1'].sum()
    
        labels1 = ['White','Black','Hispanic','Asian']
        values1 = [sum_by_state_white1, sum_by_state_black1, sum_by_state_hisp1, sum_by_state_asian1]

        fig1, ax = plt.subplots()
        ax.bar(labels1, values1, color='orange')
        ax.set_xlabel('Ethnicity')
        ax.set_ylabel('  ')
        ax.set_title('Ethnicities 1-mile from a grocery store in {}'.format(selected_state1))
        st.pyplot(fig1)

    with tab2:
        selected_state10 = st.selectbox('Select state', food_data['State'].unique(), key='tab2_selectbox')

        state_data10 = food_data[food_data['State'] == selected_state10]

        sum_by_state_white10 = state_data10['lawhite10'].sum()
        sum_by_state_black10 = state_data10['lablack10'].sum()
        sum_by_state_hisp10 = state_data10['lahisp10'].sum()
        sum_by_state_asian10 = state_data10['laasian10'].sum()
    
        labels10 = ['White','Black','Hispanic','Asian']
        values10 = [sum_by_state_white10, sum_by_state_black10, sum_by_state_hisp10, sum_by_state_asian10]

        fig10, ax = plt.subplots()
        ax.bar(labels10, values10, color='orange')
        ax.set_xlabel('Ethnicity')
        ax.set_ylabel('  ')
        ax.set_title('Ethnicities 10-miles from a grocery store in {}'.format(selected_state10))
        st.pyplot(fig10)

    with tab3:
        selected_state20 = st.selectbox('Select state', food_data['State'].unique(), key='tab3_selectbox')

        state_data20 = food_data[food_data['State'] == selected_state20]

        sum_by_state_white20 = state_data20['lawhite20'].sum()
        sum_by_state_black20 = state_data20['lablack20'].sum()
        sum_by_state_hisp20 = state_data20['lahisp20'].sum()
        sum_by_state_asian20 = state_data20['laasian20'].sum()
    
        labels20 = ['White','Black','Hispanic','Asian']
        values20 = [sum_by_state_white20, sum_by_state_black20, sum_by_state_hisp20, sum_by_state_asian20]

        fig20, ax = plt.subplots()
        ax.bar(labels20, values20, color='orange')
        ax.set_xlabel('Ethnicity')
        ax.set_ylabel('  ')
        ax.set_title('Ethnicities 10-miles from a grocery store in {}'.format(selected_state20))
        st.pyplot(fig20)
