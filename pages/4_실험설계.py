import streamlit as st
import pandas as pd

st.title("실험 설계")
st.divdier()
st.header("문항 설계 정리")
st.write("각 문항에 들어간 지식요소 및 오개념의 개수를 정리하면 다음과 같다.")
st.subheader("1")
data1 = {'1-1': [1,2],
        '1-2': [2,1],
        '1-3': [1,2],
        '1-4': [2,3],
        '1-5': [2,2],
        '1-6': [1,3],
        '1-7': [3,4],
        '1-8': [5,4]}
df1 = pd.DataFrame(data1)
df1.index = ["지식요소", "오개념"]
styled_df1 = df1.style\
    .set_properties(**{'text-align': 'center', 'font-weight': 'bold'})\
    .set_table_styles([{'selector': 'th',
                        'props': [('text-align', 'center'),
                                  ('font-weight', 'bold'),
                                  ('background-color', 'lightblue')]}])
st.table(styled_df1)
st.subheader("2")
data2 = {'2-1': [1,2],
        '2-2': [1,2],
        '2-3': [1,2],
        '2-4': [1,2],
        '2-5': [2,3],
        '2-6': [5,4],
        '2-7': [4,2],
        '2-8': [6,1],
        '2-9': [4,3]}
df2 = pd.DataFrame(data2)
df2.index = ["지식요소", "오개념"]
styled_df2 = df2.style\
    .set_properties(**{'text-align': 'center', 'font-weight': 'bold'})\
    .set_table_styles([{'selector': 'th',
                        'props': [('text-align', 'center'),
                                  ('font-weight', 'bold'),
                                  ('background-color', 'lightblue')]}])
st.table(styled_df2)
st.subheader("3")
data3 = {'3-1': [1,1],
        '3-2': [1,1],
        '3-3': [5,1]}
df3 = pd.DataFrame(data3)
df3.index = ["지식요소", "오개념"]
styled_df3 = df3.style\
    .set_properties(**{'text-align': 'center', 'font-weight': 'bold'})\
    .set_table_styles([{'selector': 'th',
                        'props': [('text-align', 'center'),
                                  ('font-weight', 'bold'),
                                  ('background-color', 'lightblue')]}])
st.table(styled_df3)

st.divdier()
st.header("실험 설계")
st.write("**대상 학년** : 중학교 2학년")
st.write("**대상 학생** : 2개 학교 241명의 학생")
st.write("**문제 풀이 시간** : 1시간")
st.write("**실험 진행 과정** : 데이터 수집 :point_right: 데이터 전처리 :point_right: 자동채점모델 생성 :point_right: 피드백 방안 만들기")
