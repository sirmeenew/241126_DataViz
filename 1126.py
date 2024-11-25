import streamlit as st
import pandas as pd
import geopandas as gpd
import folium
from streamlit_folium import st_folium
import os

# 데이터 파일 경로 설정
data_dir = "./data"
csv_path = os.path.join(data_dir, '연령별_출산율_및_합계출산율_행정구역별__20241126033905.csv')
geojson_path = os.path.join(data_dir, 'N3A_G0100000.json')

# 데이터 로드
@st.cache_data
def load_data():
    try:
        df = pd.read_csv(csv_path, header=1)
        gdf_sigungu = gpd.read_file(geojson_path)
        return df, gdf_sigungu
    except Exception as e:
        st.error(f"데이터 로드 실패: {e}")
        return None, None

df, gdf_sigungu = load_data()

# 데이터 확인
if df is not None and gdf_sigungu is not None:
    if st.checkbox("데이터 확인"):
        st.write("CSV 데이터:")
        st.dataframe(df.head())
        st.write("GeoJSON 데이터:")
        st.write(gdf_sigungu.head())

    # 지도 생성
    namhan_center = [36.34, 127.77]
    title = '전국 시군구별 합계출산율 지도'
    title_html = f'<h3 align="center" style="font-size:20px"><b>{title}</b></h3>'

    try:
        gu_map = folium.Map(
            location=namhan_center,
            zoom_start=8,
            tiles='cartodbpositron'
        )
        gu_map.get_root().html.add_child(folium.Element(title_html))

        # Choropleth 추가
        folium.Choropleth(
            geo_data=gdf_sigungu,
            data=df,
            columns=('행정구역별', '합계출산율 (가임여성 1명당 명)'),
            key_on='feature.properties.NAME',
            fill_color='BuPu',
            fill_opacity=0.7,
            line_opacity=0.5,
            legend_name='전국 시군구별 합계출산율 지도'
        ).add_to(gu_map)

        # Streamlit 앱에 지도 표시
        st.title("전국 시군구별 합계출산율")
        st_folium(gu_map, width=800, height=600)
    except Exception as e:
        st.error(f"지도 생성 실패: {e}")
else:
    st.error("데이터를 로드하지 못해 지도를 생성할 수 없습니다.")
