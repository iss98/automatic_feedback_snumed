import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

st.set_page_config(layout="wide")
st.title(":robot_face: 데이터 전처리 과정")
st.divider()
st.header(":robot_face: OCR 이용 과정에서의 문제점")
st.write("OCR 프로그램인 [mathpix](https://mathpix.com/)를 이용하여 학생들의 손글씨 응답을 LaTeX 언어로 변환하고자 하였음")
st.write("하지만 실험으로 돌렸던 OCR 결과와 달리 학생들의 글씨, 응답을 작성하는 구역 등의 문제로 OCR이 제대로 진행되지 않음")
st.subheader("OCR이 잘된 예시")
code1 = '''
등식의 성질 : 두 식 $A, B$ 가 서로 같을 때 즉 $A=B$ 일 때, 수 C에 대하여

(1) 등식의 양변에 같은 수를 더하여도 등식은 성립한다.

(2) 등식의 양변에 같은 수를 빼도 등식은 성립한다.

(3) 등식의 양변에 같은 수를 곱하여도 등식은 성립한다.

xol $x+4-c y<2) 23-(847$

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
url1 = "images/OCRexample1.jpg"
st.image(url1, caption="OCR이 잘 된 예시")
st.code(code1, language = 'latex')

st.subheader("OCR이 잘 안된 예시")
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
st.image("images/OCRexample2.jpg", caption="OCR이 잘 안된 예시")
st.code(code2, language = 'latex')
st.write("손글씨를 OCR 변환하지 않고, 직접 csv 파일에 텍스트 데이터로 옮겨적었음")
st.write(":heavy_exclamation_mark: 후속 연구에서는 데이터를 손글씨가 아닌 텍스트로 수집하거나, OCR 프로그램이 정상 작동하는 형식을 미리 준비하고 충분한 사전 테스트를 거칠 필요가 있음")
st.divider()
st.header(":robot_face: 손글씨 데이터를 텍스트 데이터로 변환시 규칙")
st.write("대부분의 선행연구에서 수학 텍스트를 분석할 때 latex 기반의 문법을 활용함. 손글씨 데이터를 텍스트 데이터로 옮기는 과정에서 latex 문법을 사용하였음.")
st.write("또한, 텍스트 데이터로 옮기는 과정에서 정오답, 지식 요소, 오개념은 답안별로 직접 채점하여 0, 1로 입력하였음")
st.markdown(r''' 1. $x \times y$ $\Rightarrow$ x \times y''')
st.markdown('2. $x \div y$ $\Rightarrow$ x \div y')
st.markdown(r'''3. $\frac{a}{b}$ $\Rightarrow$ a/b''')
st.divider()


st.header(":robot_face: 데이터 예시")
st.write("데이터를 csv파일로 옮긴 예시")
option = st.selectbox(
    '문제 번호를 골라주세요',
    ("1-8","3-3"))
df = pd.read_csv("./save/"+option+".csv")
df = df.dropna(subset = ["답안"])
num_rows = len(df)
st.write(f"응답을 한 학생 수 : {num_rows}, 총 학생 수 : 241")
st.dataframe(df)

column_distributions = {}
for column in df.columns[2:]:
    column_distributions[column] = df[column].values

st.set_option('deprecation.showPyplotGlobalUse', False) 

col1, col2 = st.columns(2)

col_list = list(column_distributions.keys())
slice_ind = len(col_list)//2

with col1:
    for column in col_list[:slice_ind]:
        values = column_distributions[column]
        st.subheader(f'Column: {column}')
        counts, bins, _ = plt.hist(values, bins='auto', edgecolor='black', linewidth=1.2, color='#4287f5', alpha=0.8)
        percentages = counts / sum(counts) * 100
        plt.clf()
        plt.bar(bins[:-1], percentages, width=np.diff(bins), align='edge', color='#4287f5', alpha=0.8)
        plt.ylabel('Percentage')
        plt.title('Distribution')
        plt.grid(axis='y', linestyle='--', alpha=0.5)
        plt.xticks(fontsize=8)
        plt.yticks(fontsize=8)
        st.pyplot()

with col2:
    for column in col_list[slice_ind:]:
        values = column_distributions[column]
        st.subheader(f'Column: {column}')
        counts, bins, _ = plt.hist(values, bins='auto', edgecolor='black', linewidth=1.2, color='#4287f5', alpha=0.8)
        percentages = counts / sum(counts) * 100
        plt.clf()
        plt.bar(bins[:-1], percentages, width=np.diff(bins), align='edge', color='#4287f5', alpha=0.8)
        plt.ylabel('Percentage')
        plt.title('Distribution')
        plt.grid(axis='y', linestyle='--', alpha=0.5)
        plt.xticks(fontsize=8)
        plt.yticks(fontsize=8)
        st.pyplot()

st.subheader("데이터 분포의 특징")
st.write(":one: 문항 설계의 단계에서 고려한 여러 가지의 풀이 중 학생들이 특정 풀이를 선호하는 경향성이 보임")
st.write("3-3의 경우 (다항식)X(단항식)을 사용해 문제를 푼 학생들이 (다항식)$\div$(단항식)를 사용해 푼 학생들보다 훨씬 많았음")
st.write(":two: 대부분의 데이터들이 편향되게 분포하였음")
st.write("3-1 ~ 3-3 문항의 경우 문제를 푼 학생들의 정답률이 90%였음. 모델이 1로만 응답을 해도 정답률이 90%가 나오는 상황")
st.write("또한, 오개념을 보인 학생의 수가 많지 않았음")