import streamlit as st

st.set_page_config(layout="wide")
st.title("대표 문항 설계")
st.divider()
st.header("1-7")
st.write(r"**문제** : $(2^4)^x \times (2^3)^x = 2^3 \times 2^{3x}$")
st.write("**지식요소** : 거듭제곱의 거듭제곱, 거듭제곱의 곱셈, 일차방정식의 풀이")
latex_equation1 = r"""
모범답안1
\begin{equation}
\begin{split}
    2^{4x} \times 2^{2x} & = 2^3 \times 2^{3x} ~ \text{거듭제곱의 거듭제곱} \\
    2^{6x} & = 2^{3+3x} ~ \text{거듭제곱의 곱셈} \\
    6x & = 3+3x ~ \text{일차방정식의 풀이} \\
    x & = 1 \\
\end{split}
\end{equation}
"""
latex_equation2 = r"""
**모범답안1**
\begin{equation}
\begin{split}
    2^{4x} \times 2^{2x} & = 2^3 \times 2^{3x} ~ \text{거듭제곱의 거듭제곱} \\
    2^{6x} & = 2^{3+3x} ~ \text{거듭제곱의 곱셈} \\
    6x & = 3+3x ~ \text{일차방정식의 풀이} \\
    x & = 1 \\
\end{equation}
\end{split}
**모범답안2**
\begin{equation}
\begin{split}
    2^{6x} & = 2^{3+3x} ~ \text{거듭제곱의 거듭제곱, 거듭제곱의 곱셈} \\
    6x & = 3+3x ~ \text{일차방정식의 풀이} \\
    x & = 1 \\
\end{equation}
\end{split}
**모범답안3**
\begin{equation}
\begin{split}
    2^{6x} & = 2^{3+3x} ~ \text{거듭제곱의 거듭제곱, 거듭제곱의 곱셈} \\
    x & = 1 \\
\end{equation}
\end{split}
"""
st.latex(latex_equation1)
st.write("**지식맵**")
st.write("지식맵 들어가는 곳")
st.write("**오개념**")
st.write("1. 등호오류 : 거듭제곱과 지수의 계산을 혼동하는 것으로 보임, 등호를 계산 진행과정 사이에 사용함, 논리적 오류가 없는 부분도 있지만 등호를 계산 진행 과정 사이에 사용함")
st.write("\left ( 2^4 right )^x times \left ( 2^2 right )^x = 2^3 times 2^{ 3x } **=** 2^{ 4x } times 2^{ 2x } = 2^3 times 2^{ 3x } **=** 2^{ 3x } = 2^3")
st.write("2. 식오류 : 곱셈 기호를 덧셈 기호로 혼동하여 작성함, 중간에 옮겨적는 과정에서 수나 문자를 잘못 적음, 지수에 있는 미지수를 빼고 계산함")
st.write("<strong> 2^4 times 2^2 = 2^3 times 2^3 = 16 times 4 = 8 times 8</strong>  x = 1")
st.write("3. 이항오개념 : 등식의 성질을 이용하여 양변에 2^{3x}를 나눈 것인데 이항이라는 용어로 표현함")
st.write("\left { 2^6 right }^x = 2^3 times 2^{ 3x }  <strong>이항</strong>  2^{ 3x } = 2^3")
st.write("4. 대입으로 해결 : 오류는 아니지만 이 문제에서 평가하고자 하는 요소가 아닌 대입으로 해결함")