
import pandas as pd #pandas 라이브러리 불러오기

df = pd.read_csv('./data/연령별_출산율_및_합계출산율_행정구역별__20241126033905.csv', header=1) #전국 시군구별 합계출산율 데이터 불러오기
df.head()

import geopandas as gpd #geopandas 라이브러리 불러오기

gdf_sigungu = gpd.read_file('./N3A_G0100000.json') 
gdf_sigungu.head() #데이터 출력하기

import folium #folium 불러오기

namhan_center = [36.34, 127.77] #대한민국 중심 좌표

title = '전국 시군구별 합계출산율 지도'
title_html = f'<h3 align="center" style="font-size:20px"><b>{title}</b></h3>'

gu_map = folium.Map(
location=namhan_center,
zoom_start=8,
tiles='cartodbpositron'
)

gu_map.get_root().html.add_child(folium.Element(title_html))


folium.Choropleth(
  geo_data=gdf_sigungu,
  data=df,
  columns= ('행정구역별',	'합계출산율 (가임여성 1명당 명)'),
  key_on='feature.properties.NAME',
  fill_color='BuPu',
  fill_opacity=0.7,
  line_opacity=0.5,
  legend_name='전국 시군구별 합계출산율 지도'
).add_to(gu_map)

gu_map
