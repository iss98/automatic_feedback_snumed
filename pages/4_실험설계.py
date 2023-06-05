import streamlit as st
import pandas as pd

st.set_page_config(layout="wide")
st.title(":test_tube: 실험 설계")
st.divider()

st.header(":test_tube: 실험 설계")
st.write("**대상 학년** : 중학교 2학년")
st.write("**대상 학생** : 2개교 학생(241명)")
st.write("**단원** : 중학교 2-1 식의 계산")
st.write("**문제 풀이 시간** : 40분")
st.write("**데이터 형태** : 디벗(갤럭시 탭)을 사용하여 준비된 답안지 pdf 양식에 답안을 작성")
st.write("**실험 진행 과정** : ")
st.write("**단원 및 대상 선정** :")
st.write(":point_right: 지식맵 작성") 
st.write(":point_right: 문항 설계")
st.write(":point_right: 루브릭 작성 (예상 답안, 답안 요소별 지식요소, 오개념)")
st.write(":point_right: 데이터 수집")
st.write(":point_right: 데이터 전처리") 
st.write(":point_right: 자동채점 모델 생성") 
st.write(":point_right: 피드백 방안 만들기")