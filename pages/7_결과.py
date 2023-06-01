import streamlit as st

st.set_page_config(layout="wide")
st.title("결과정리")
st.divider()
st.header("1. 지식요소 모델")
st.subheader("파트1")
col1, col2, col3 = st.columns(3)

with col1:
    st.image('images/1_1_acc.jpg', use_column_width=True, caption = "Accuracy")
    st.image('images/1_4_1_7_acc.jpg', use_column_width=True, caption = "Accuracy")

with col2:
    st.image('images/1_1_loss.jpg', use_column_width=True, caption = "loss")
    st.image('images/1_4_1_7_loss.jpg', use_column_width=True, caption = "loss")

with col3:
    st.image('images/1_1_testacc.jpg', use_column_width=True, caption = "Test Accuracy")
    st.image('images/1_4_1_7_testacc.jpg', use_column_width=True, caption = "Test Accuracy")
markdown_table1 = """
|  | **1-1** | **1-2** | **1-3** | **1-4** | **1-5** | **1-6** | **1-7** | **1-8** |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| RNN | |  | | | | | | |
| LSTM | |  | | | | | | |
| Attention | | | | | | | | |
"""
st.markdown(markdown_table1, unsafe_allow_html=True)
st.write("결과 정리")

st.subheader("파트2")
col4, col5, col6 = st.columns(3)

with col4:
    st.image('images/1_2_acc.png', use_column_width=True, caption = "Accuracy")
    st.image('images/2_1_2_6_acc.png', use_column_width=True, caption = "Accuracy")

with col5:
    st.image('images/1_2_loss.png', use_column_width=True, caption = "loss")
    st.image('images/2_1_2_6_loss.png', use_column_width=True, caption = "loss")

with col6:
    st.image('images/1_2_testacc.png', use_column_width=True, caption = "Test Accuracy")
    st.image('images/2_1_2_6_testacc.png', use_column_width=True, caption = "Test Accuracy")
markdown_table2 = """
|  | **2-1** | **2-2** | **2-3** | **2-4** | **2-5** | **2-6** | **2-7** | **2-8** | **2-9**|
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| RNN | |  | | | | | | | |
| LSTM | |  | | | | | | | |
| Attention | | | | | | | | | |
"""
st.markdown(markdown_table2, unsafe_allow_html=True)
st.write("결과 정리")
st.subheader("파트3")
col7, col8, col9 = st.columns(3)

with col7:
    st.image('images/1_3_acc.png', use_column_width=True, caption = "Accuracy")
with col8:
    st.image('images/1_3_loss.png', use_column_width=True, caption = "loss")
with col9:
    st.image('images/1_3_testacc.png', use_column_width=True, caption = "Test Accuracy")
markdown_table3 = """
|  | **3-1** | **3-2** | **3-3** |
| --- | --- | --- | --- |
| RNN | |  | |
| LSTM | |  | |
| Attention | | | |
"""
st.markdown(markdown_table3, unsafe_allow_html=True)
st.write("결과 정리")    
st.divider()
st.header("2. 오개념 모델")

col10, col11, col12 = st.columns(3)
with col10 :
    st.image('images/2_1_acc.png', use_column_width=True, caption = "Accuracy")
    st.image('images/2_2_acc.png', use_column_width=True, caption = "Accuracy")
    st.image('images/2_3_acc.png', use_column_width=True, caption = "Accuracy")
with col11:
    st.image('images/2_1_loss.png', use_column_width=True, caption = "loss")
    st.image('images/2_2_loss.png', use_column_width=True, caption = "loss")
    st.image('images/2_3_loss.png', use_column_width=True, caption = "loss")
with col12:
    st.image('images/2_1_testacc.png', use_column_width=True, caption = "Test Accuracy")
    st.image('images/2_2_testacc.png', use_column_width=True, caption = "Test Accuracy")
    st.image('images/2_3_testacc.png', use_column_width=True, caption = "Test Accuracy")

markdown_table4 = """
|  | **1-1** | **1-2** | **1-3** | **1-4** | **1-5** | **1-6** | **1-7** | **1-8** |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| RNN | |  | | | | | | |
| LSTM | |  | | | | | | |
| Attention | | | | | | | | |
"""
st.markdown(markdown_table4, unsafe_allow_html=True)
markdown_table5 = """
|  | **2-1** | **2-2** | **2-3** | **2-4** | **2-5** | **2-6** | **2-7** | **2-8** | **2-9**|
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| RNN | |  | | | | | | | |
| LSTM | |  | | | | | | | |
| Attention | | | | | | | | | |
"""
st.markdown(markdown_table5, unsafe_allow_html=True)
markdown_table6 = """
|  | **3-1** | **3-2** | **3-3** |
| --- | --- | --- | --- |
| RNN | |  | |
| LSTM | |  | |
| Attention | | | |
"""
st.markdown(markdown_table6, unsafe_allow_html=True)
st.write("결과 정리")

st.divider()
st.header("3. 정오답 채점 모델")

col13, col14, col15 = st.columns(3)
with col13 :
    st.image('images/all_acc.png', use_column_width=True, caption = "Accuracy")
with col14 :
    st.image('images/all_loss.png', use_column_width=True, caption = "loss")
with col15 : 
    st.image('images/all_tesetacc.png', use_column_width=True, caption = "Test Accuracy")
markdown_table7 = """
|  | **ALL** |
| --- | --- |
| **RNN** | **0.958** | 
| **LSTM** | 0.840 |  
| **Attention** | 0.856 |
"""
st.markdown(markdown_table7, unsafe_allow_html=True)
st.write("결과 정리")