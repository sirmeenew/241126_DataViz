import streamlit as st
import pandas as pd
import geopandas as gpd
import folium
from streamlit_folium import folium_static

# CSV 파일 로드 (출산율 데이터)
df = pd.read_csv('./연령별_출산율_및_합계출산율_행정구역별__20241126033905.csv', header=1)

# GeoJSON 파일 로드 (행정구역 데이터)
gdf_sigungu = gpd.read_file('./N3A_G0100000.json')

# 지도 설정 (대한민국 중심)
namhan_center = [36.34, 127.77]

# 지도 제목
title = '전국 시군구별 합계출산율 지도'
title_html = f'<h3 align="center" style="font-size:20px"><b>{title}</b></h3>'

# Folium 지도 생성
gu_map = folium.Map(
    location=namhan_center,
    zoom_start=8,
    tiles='cartodbpositron'
)

# 제목 추가
gu_map.get_root().html.add_child(folium.Element(title_html))

# Choropleth Layer 추가
folium.Choropleth(
    geo_data=gdf_sigungu,
    data=df,
    columns=('행정구역별', '합계출산율 (가임여성 1명당 명)'),  # 데이터 컬럼명
    key_on='feature.properties.NAME',  # GeoJSON 속성 매칭
    fill_color='BuPu',  # 색상 설정
    fill_opacity=0.7,
    line_opacity=0.5,
    legend_name='전국 시군구별 합계출산율'
).add_to(gu_map)

# Streamlit에 Folium 지도 렌더링
st.title("전국 시군구별 합계출산율")
folium_static(gu_map)
