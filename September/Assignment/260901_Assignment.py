import streamlit as st
import pandas as pd

# 자동차 데이터 불러오기
df = pd.read_csv("cars.csv")  # 실제 데이터 파일 경로로 변경 필요

st.title("자동차 데이터")
st.write("#### :green[자동차 데이터 테이블]")

manufacturers = df['Manufacturer'].to_list()
manufacturer = st.selectbox("제조사 선택", manufacturers)
selected = df[df['Manufacturer'] == manufacturer] 

sort_column = st.selectbox("정렬할 컬럼 선택", df.columns)

direction = st.radio("정렬 순서 선택", ("오름차순", "내림차순"))
if direction == "오름차순":
    direction = True
else:
    direction = False

st.dataframe(selected.sort_values(by=sort_column, ascending=direction))