import streamlit as st

st.set_page_config(layout="wide")
st.title(":thinking_face: 결과정리")
st.write("일부 문항은 tokenizer로 bw를 사용하였을 때 학습모델이 제대로 구동되지 않는 경우가 있음")
st.write("이에 tokenizer는 sp로 사용하여 3가지 모델을 학습한 결과를 다음과 같이 얻음")
st.divider()
st.header(":one: 지식요소 모델")
st.subheader("Part1")
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
| RNN | **0.956** | 0.921 | 0.851 | 0.844 | 0.900 | **0.979** | 0.731 | 0.586 |
| LSTM | 0.914 | **0.972**  | 0.924 | 0.816 | **0.950** | 0.853 | **0.766** | **0.744**|
| Attention | 0.979 | 0.921 | **0.879** | **0.849** | 0.944 | 0.876 | 0.670 | 0.706 |
"""
st.write(":star: Accuracy table")
st.markdown(markdown_table1, unsafe_allow_html=True)
st.write("")

st.subheader("Part2")
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
| RNN | 0.957 | 0.945 | 0.896 | 0.896 | **0.861** | 0.628 | 0.908 | 0.741 | 0.797 | 
| LSTM | **0.978** | **0.948** | **0.958** | 0.881 | 0.810 | 0.706 | 0.888 | **0.817** | 0.834 |
| Attention | 0.948 | 0.850 | 0.884 | **0.912** | 0.840 | **0.712** | **0.938** | 0.769 | **0.843**|
"""
st.write(":star: Accuracy table")
st.markdown(markdown_table2, unsafe_allow_html=True)
st.write("")

st.subheader("Part3")
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
| RNN | 0.948 | 0.958 | **0.895** |
| LSTM | **1.000** | **0.969** | 0.854 |
| Attention | 0.938 | 0.875 | 0.860 |
"""
st.write(":star: Accuracy table")
st.markdown(markdown_table3, unsafe_allow_html=True)
st.write("")
st.write("**결과 정리**")
st.write(":one: 3-1과 같이 답안이 간단한 문항의 경우 1에 가까운 accuracy를 보이기도 했지만, 답안이 가장 복잡한 1-8과 같은 경우는 0.7 정도의 accuracy를 나타냄")
st.write(":two: 최적 모델은 문항마다 상이하며, 전체적으로 유의미한 정도의 차이를 나타내지는 않음")      
st.divider()
st.header(":two: 오개념 모델")

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
| RNN | 0.972 | 0.938 | 0.921 | **0.926** | **0.957** | 0.926 | **0.938** | 0.900 |
| LSTM | 0.964 | 0.921 | 0.935 | 0.925 | **0.957** | **0.947** | **0.938** | 0.896 |
| Attention | **0.986** | **0.948** | **0.950** | 0.922 | 0.956 | 0.940 | 0.916 | **0.924** |
"""
st.write(":star: Accuracy table")
st.markdown(markdown_table4, unsafe_allow_html=True)
st.write("")
markdown_table5 = """
|  | **2-1** | **2-2** | **2-3** | **2-4** | **2-5** | **2-6** | **2-7** | **2-8** | **2-9**|
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| RNN | **0.986** | **0.984** | **0.965** | 0.951 | **0.965** | 0.850 | 0.794 | **0.927**| 0.929|
| LSTM | 0.963 | 0.977 | 0.951 | **0.962** | 0.943 | 0.847 | **0.888** | 0.924 | **0.949**|
| Attention | 0.963 | 0.949 | 0.889 | 0.947 | 0.944 | **0.858** | **0.888** | 0.898 | 0.928 |
"""
st.write(":star: Accuracy table")
st.markdown(markdown_table5, unsafe_allow_html=True)
st.write("")
st.write(":star: Accuracy table")
markdown_table6 = """
|  | **3-1** | **3-2** | **3-3** |
| --- | --- | --- | --- |
| RNN | **0.990**| **0.979** | 0.878 |
| LSTM | 0.979 | 0.969 | **0.896** |
| Attention | 0.911 | **0.979** | 0.819|
"""
st.markdown(markdown_table6, unsafe_allow_html=True)
st.write("")
st.write("**결과 정리**")
st.write(":one: 오개념의 경우 지식요소보다 label의 개수가 적어 비교적 높은 accuracy를 보임(분포와도 연관이 있을 것으로 보임)")
st.write(":two: 최적 모델은 문항마다 상이하며, 전체적으로 유의미한 정도의 차이를 나타내지는 않음")         

st.divider()
st.header(":three: 정오답 채점 모델")

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
st.write(":star: Accuracy table")
st.markdown(markdown_table7, unsafe_allow_html=True)
st.write("")
st.write("**결과 정리**")
st.write(":one: 전 문항에 대한 정오답 모델의 경우 RNN 모델이 다른 모델에 비해 상대적으로 높은 accuracy와 낮은 loss를 보여 보다 적합하다고 판단됨")
st.write(":thinking_face: 과적합이 될 수 밖에 없어서 그런게 아닐까?")      