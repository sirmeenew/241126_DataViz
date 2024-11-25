import streamlit as st
from streamlit_folium import st_folium
import folium

# Streamlit 제목
st.title("Folium Map in Streamlit")

# Folium 지도 생성
m = folium.Map(location=[37.5665, 126.9780], zoom_start=12)  # 서울의 중심 좌표로 설정

# 지도에 마커 추가
folium.Marker([37.5665, 126.9780], popup="Seoul", tooltip="Click me!").add_to(m)

# Streamlit에서 Folium 지도 렌더링
st_folium(m, width=725)
