import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

st.set_page_config(layout="wide")
st.title("데이터 전처리 과정")
st.divider()
st.header("OCR 이용 과정에서의 문제점")
st.write("OCR 프로그램인 [mathpix](https://mathpix.com/)를 이용하여 학생들의 손글씨 응답을 LaTeX 언어로 변환하고자 하였음")
st.write("하지만 실험적으로 돌렸던 OCR 결과와 달리 학생들의 글씨, 응답을 작성하는 구역 등의 문제로 OCR이 제대로 진행되지 않음")
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
url1 = "images/OCRexample1.png"
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
url2 = "iamges/OCRexample2.png"
st.image(url2, caption="OCR이 잘 안된 예시")
st.code(code2, language = 'latex')
st.write("손글씨를 OCR 변환하지 않고, 직접 csv 파일에 텍스트 데이터로 옮겨적었음")
st.divider()
st.header("손글씨 데이터를 텍스트 데이터로 변환시 규칙")
st.markdown(r''' 1. $x \times y$ $\Rightarrow$ x \times y''')
st.markdown('2. $x \div y$ $\Rightarrow$ x \div y')
st.markdown(r'''3. $\frac{a}{b}$ $\Rightarrow$ a/b''')
st.divider()

st.header("데이터 예시")
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

for column, values in column_distributions.items():
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

st.write("데이터의 분포 관련 설명 추가")