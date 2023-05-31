import streamlit as st

st.title("데이터 전처리 과정")
st.header("OCR 이용 과정에서의 문제점")
st.write("OCR 프로그램인 [mathpix](https://mathpix.com/)를 이용하여 학생들의 손글씨 응답을 LaTeX 언어로 변환하고자 하였음")
st.write("하지만 실험적으로 돌렸던 OCR 결과와 달리 학생들의 글씨, 응답을 작성하는 구역 등의 문제로 OCR이 제대로 진행되지 않음")
st.subheader("OCR이 잘된 예시")
code1 = '''\begin{document}
\begin{center}
\includegraphics[max width=\textwidth]{2023_03_15_f3afde196b324d7e7b05g-1(3)}
\end{center}

구글클래스룸 영상

등식의 성질 : 두 식 $A, B$ 가 서로 같을 때 즉 $A=B$ 일 때, 수 C에 대하여

(1) 등식의 양변에 같은 수를 더하여도 등식은 성립한다.

(2) 등식의 양변에 같은 수를 빼도 등식은 성립한다.

(3) 등식의 양변에 같은 수를 곱하여도 등식은 성립한다.

xol $x+4-c y<2) 23-(847$

$$
\begin{aligned}
& x^{2} 3-4 \\
& x^{2}-1
\end{aligned}
$$

문제2, 3. (98p, 99p) 등식의 성질을 이용하여 다음 방정식을 푸세요.

(1) $x-3=6$ eㅐ

(2) $3 x+1=10 \quad \boldsymbol{X} \boldsymbol{\mho}$

(3) $x+5=-2 \boldsymbol{x}_{2} \boldsymbol{\eta}$

(4) $3 x-7=5 x<4$

(5) $-4 x=x+6 \quad x 2-\frac{6}{6}$

(6) $3+x=-2 x$ xr 1

방정식의 해를 구하는 연습을 해봅시다. “이낳 " 이용하기!

문제2, 3. (98p, 99p) 이항을 이용하여 다음 방정식을 푸세요.

(1) $x-3=6 x 29$

(2) $3 x+1=10 x 23$

(3) $x+5=-2 x \chi^{\boldsymbol{M}}$

(4) $3 x-7=5 \quad x=4$

(5) $-4 x=x+6 x=-\frac{6}{6}$

(6) $3+x=-2 x x=1$

일차방정식 푸는 것을 연습해봅시다.

\begin{center}
\includegraphics[max width=\textwidth]{2023_03_15_f3afde196b324d7e7b05g-2}
\end{center}

문제 무한 연습 (101p 104p) 다음 식을 계산하세요.

(1) $7 x+10=-4$ xr

(2) $3-4 x=x+18 x^{2}-3$

(3) $3(x-5)=9+x$ prð

(4) $-4(x+5)=24 \boldsymbol{x}_{2}-11$

(5) $-2 x+5(x-1)=10 x>5$

(6) $-(8 x-6)=7(2-x) x^{2}-8$

(7) $0.6 x+3.5=-0.7 x^{2}-1$

(8) $0.1-0.04 x=0.03 x+0.31 x z-3$

(9) $\frac{3}{2} x+1=\frac{2}{5} x-\frac{1}{10} \times 2-1$

(10) $\frac{5 x+2}{6}=\frac{x+10}{3}-2 \not c=-1$
'''
st.code(code1, language = 'latex')

st.subheader("OCR이 잘못된 예시")
code2 = '''\begin{document}
\begin{center}
\includegraphics[max width=\textwidth]{2023_04_26_2b23690b9474cb154cf5g-1(1)}
\end{center}

8

\begin{center}
\includegraphics[max width=\textwidth]{2023_04_26_2b23690b9474cb154cf5g-1}
\end{center}

\begin{center}
\includegraphics[max width=\textwidth]{2023_04_26_2b23690b9474cb154cf5g-2}
\end{center}'''
st.code(code2, language = 'latex')
st.write("손글씨를 OCR 변환하지 않고, 직접 csv 파일에 텍스트 데이터로 옮겨적었음")

st.header("손글씨 데이터를 텍스트 데이터로 변환시 규칙")
st.latex(r'''
1. $x \times y$ $\Rightarrow$ x \times y
2. $x \div y$ $\Rightarrow$ x \div y
3. $\frac{a}{b}$ $\Rightarrow$ a/b
''')