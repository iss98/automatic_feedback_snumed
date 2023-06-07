import streamlit as st

st.set_page_config(layout="wide")

st.header("📚문항 설계의 전반적인 원리")
st.divider()
st.header("📚문항 설계 목표")
st.write("\n\n    1. 식의 계산 단원에서 학생들이 가지고 있는 인지 요소 분석")
st.write("    2. 식의 계산 단원에서 학생들이 가지고 있는 오개념 분석 ")
st.divider()
st.header("📚단원 선택 이유")
st.write("\n\n    1. 중학교 2학년 대상의 자료 수집 용이")
st.write("    2. 지식맵의 위계성이 뚜렷한 단원으로 선정")
st.write("    3. 다양한 오개념이 존재하며 오개념이 풀이과정에서 잘 드러남")



st.divider()
st.header("📚문항 설계 방식")
st.markdown("- 지식맵의 상위 요소부터 고려 \n\n - 각 인지요소에 해당하는 문항이 한 개 이상 들어가도록 개발 \n\n - 문항별 다양한 풀이과정 고려")
st.markdown("- 총 20개 문항 제작 \n\n   - 13개는 단답형 형식으로 대답 가능한 문항 \n\n   - 7개는 복잡한 답안이 예상되는 문항")
st.markdown("- 총 세 파트로 분류 \n\n   - Part1: 거듭제곱의 곱셈, 거듭제곱의 거듭제곱, 거듭제곱의 나눗셈, 곱의 거듭제곱과 분수의 거듭제곱  \n\n   - Part2: 단항식의 곱셈과 나눗셈, 다항식의 덧셈과 뺄셈  \n\n    - Part3: 단항식과 다항식의 곱셈과 나눗셈")

st.divider()
st.header("📚식의 계산 단원 내 지식맵 구성")
st.image("images/all.png")