import streamlit as st
from streamlit_folium import st_folium
import folium

# Streamlit 제목
st.title("Folium Map in Streamlit Cloud")

# Folium 지도 생성
m = folium.Map(location=[37.5665, 126.9780], zoom_start=12)  # 서울 좌표

# Folium 지도 렌더링
st_folium(m, width=700, height=500)
