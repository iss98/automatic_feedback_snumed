import streamlit as st

st.set_page_config(layout="wide")
st.title("결과정리")
st.divider()
st.header("1. 지식요소 모델")
st.subheader("파트1")
col1, col2, col3 = st.beta_columns(3)

with col1:
    st.image('../images/1_1_acc.png', use_column_width=True)
    st.image('../images/1_4_1_7_acc.png', use_column_width=True)

with col2:
    st.image('../images/1_1_loss.png', use_column_width=True)
    st.image('../images/1_4_1_7_loss.png', use_column_width=True)

with col3:
    st.image('../images/1_1_testacc.png', use_column_width=True)
    st.image('../images/1_4_1_7_testacc.png', use_column_width=True)

st.subheader("파트2")
st.subheader("파트3")
st.divider()
st.header("2. 오개념 모델")
st.subheader("파트1")
st.subheader("파트2")
st.subheader("파트3")
st.divider()
st.header("3. 정오답 채점 모델")
st.subheader("파트1")
st.subheader("파트2")
st.subheader("파트3")