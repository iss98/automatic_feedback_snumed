import streamlit as st
import pandas as pd

st.set_page_config(layout="wide")
st.header(":female-teacher: 문항 루브릭")
st.subheader("Part 1 거듭제곱")
st.image('images/part1_rubric.png', use_column_width=True, caption = "part1_rubric")
st.subheader("Part 2 단항식의 곱셈과 나눗셈, 다항식의 덧셈과 뺄셈")
st.image('images/part2_rubric.png', use_column_width=True, caption = "part2_rubric")
st.subheader("Part 3 단항식과 다항식의 곱셈 나눗셈")
st.image('images/part3_rubric.png', use_column_width=True, caption = "part3_rubric")

st.divider()
st.header(":female-teacher: 문항 설계 정리")
st.write("각 문항에 들어간 지식요소 및 오개념의 개수를 정리하면 다음과 같음")
st.write("각 문항에 최소한 1개의 지식요소와 오개념이 들어가도록 설계함")
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

st.divider()