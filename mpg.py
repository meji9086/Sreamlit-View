import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import koreanize_matplotlib
import plotly.express as px

st.set_page_config(
    page_title="Likelion AI School 자동차 연비 App",
    page_icon="🚗",
    layout="wide",
)

st.markdown("# 자동차 연비 🚗")
st.sidebar.markdown("# 자동차 연비 🚗")

url = "https://raw.githubusercontent.com/mwaskom/seaborn-data/master/mpg.csv"

@st.cache
def load_data(url):
   data = pd.read_csv(url)
   return data

data_load_state = st.text('Loading data...')
data = load_data(url)
data
data_load_state.text("Done! (using st.cache)")

st.sidebar.header('User Input Features')
selected_year = st.sidebar.selectbox('Year',
   list(reversed(range(data.model_year.min(),data.model_year.max())))
   )

sorted_unique_origin = sorted(data.origin.unique())
selected_origin = st.sidebar.multiselect('origin', sorted_unique_origin, sorted_unique_origin)


if selected_year > 0 :
   mpg = data[data.model_year == selected_year]

if len(selected_origin) > 0:
   mpg = data[data.origin.isin(selected_origin)]

st.line_chart(data["mpg"])

st.bar_chart(data["mpg"])

pxh = px.histogram(data, x='origin')
pxh

fig, ax = plt.subplots()
sns.barplot(data=data, x="origin", y="mpg").set_title("origin 별 자동차 연비")
st.pyplot(fig)

fig, ax = plt.subplots()
sns.scatterplot(data=data, x="mpg", y="weight", hue='origin').set_title("mpg 별 origin 별 weight 시각화")
st.pyplot(fig)