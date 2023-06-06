import streamlit as st
import pandas as pd

st.set_page_config(layout="wide")

st.title(":school: 대표 문항 설계")
###1-7
st.divider()
st.header(":school: 1-7")
st.write("📖식을 정리하기 위해 거듭제곱의 거듭제곱과 거듭제곱의 곱셈을 적절히 사용할 수 있는가?")
st.write("📖지수의 미지수를 구하기 위해 일차방정식의 풀이를 적절히 사용할 수 있는가?")
st.write("👉**문제** : $ (2^4)^x \\times (2^3)^x = 2^3 \\times 2^{3x} $ 일 때, 자연수 $x$의 값을 구하시오")
st.write("👉**지식요소** : 거듭제곱의 거듭제곱, 거듭제곱의 곱셈, 일차방정식의 풀이")

st.write("👉**모범답안1**")

image_url = 'save/사진자료/1-7 모범답안1.png'
st.image(image_url)

st.write("👉**모범답안2**")

image_url = 'save/사진자료/1-7 모범답안2.png'
st.image(image_url)


st.write("👉**모범답안3**")

image_url = 'save/사진자료/1-7 모범답안3.png'
st.image(image_url)


st.write("👉**지식맵**")
image_url = 'save/사진자료/1-7 지식맵.png'
st.image(image_url)

st.write("👉**오개념**")
st.markdown('<span style="color: blue;">1. 등호오류</span>', unsafe_allow_html=True)
st.markdown('<span style="color: blue;">⚠️1-1. 거듭제곱과 지수의 계산을 혼동하는 것으로 보임</span>', unsafe_allow_html=True)
st.write("예 : $(2^{4})^{x} \\times ( 2^{2})^{x} = 2^{3} \\times 2^{ 3x } = x = 1$")
st.write("예 : $2^{ 4 \\times x } \\times 2^{ 2 \\times x } = 2^{3} \\times 2^{ 3x } = 2^{ 4x + 2x } = 2^{ 3x + 3 } = 6x = 3x + 3$ ")


st.markdown('<span style="color: blue;">⚠️1-2. 등호를 계산 진행과정 사이에 사용함</span>', unsafe_allow_html=True)
st.write("예 : $(2^{4})^{x} \\times (2^{2})^{x} = 2^{3} \\times 2^{ 3x } = 2^{ 4x } \\times 2^{ 2x } = 2^{3} \\times 2^{ 3x } = 2^{ 3x } = 2^{3}$")

st.markdown('<span style="color: blue;">⚠️1-3. 논리적 오류가 없는 부분도 있지만 등호를 계산 진행 과정 사이에 사용함</span>', unsafe_allow_html=True)
st.write("예 : $(2^{4})^{x} \\times (2^{2})^{x} = 2^{3} \\times (2^{3})^{x} = 2^{ 4x } \\times 2^{ 2x } = 2^{3} \\times 2^{ 3x } = 2^{ 6x } \\div 2^{ 3x } = 2^3 = 2^{ 3x } = 2^{3} $")

st.markdown('<span style="color: blue;">2. 식 오류</span>', unsafe_allow_html=True)
st.markdown('<span style="color: blue;">⚠️2-1. 곱셈 기호를 덧셈 기호로 혼동하여 작성함</span>', unsafe_allow_html=True)
st.write("예 : $2^{ 4x } \\times 2^{ 2x } = 2^{ 6x }$, $2^{ 6x } = 2^3 + 2^{ 3x }$")

st.markdown('<span style="color: blue;">⚠️2-2. 중간에 옮겨적는 과정에서 수나 문자를 잘못 적음</span>', unsafe_allow_html=True)
st.write("예 : $( 2^{4})^{x} \\times ( 2^{2})^{x} = 2^{3} \\times 2^{ 3x }$, $2^{ 4x } \\times 2^{ 2x } = 2^3 \\times 2^{x}$")
st.write("예 : $( 2^{4})^{x} \\times ( 2^{2})^{x} = 2^{ 4x } \\times 2^{ 2x } = 2^{ 6x } = 2^{ 3x } \\times 2^{ 3x }$")
st.write("예 : $x^{ 4x } \\times 2^{ 2x } = 2^{ 3 + 3x }$")

st.markdown('<span style="color: blue;">⚠️2-3. 지수에 있는 미지수를 빼고 계산함</span>', unsafe_allow_html=True)
st.write("예 : $2^{4} \\times 2^{2} = 2^{3} \\times 2^{3} = 16 \\times 4 = 8 \\times 8$, $x = 1$")

st.markdown('<span style="color: blue;">3. 이항오개념</span>', unsafe_allow_html=True)

st.markdown('<span style="color: blue;">⚠️3-1. 등식의 성질을 이용하여 양변에 2^{3x}를 나눈 것인데 이항이라는 용어로 표현함</span>', unsafe_allow_html=True)
st.write("예 : ${ 2^{6}}^{x} = 2^{3} \\times 2^{ 3x }$ 이항 $2^{ 3x } = 2^{3}$")

st.markdown('<span style="color: blue;">4. 대입으로 해결</span>', unsafe_allow_html=True)
st.markdown('<span style="color: blue;">⚠️4-1. 오류는 아니지만 이 문제에서 평가하고자 하는 요소가 아닌 대입으로 해결함</span>', unsafe_allow_html=True)
st.write("예 : $x$에 1 대입  $2^{ 4 \\times 1 } \\times 2^{ 2 \\times 1}$, $2^{6}=2^{3}\\times2^{3\\times 1 }$, $2^{4} \\times 2^{2} = 2^{6}$, $2^{6} = 2^{6}$, 1")
st.write("예 : $( 2^{4})^{1} \\times ( 2^{2})^{1} = 2^{3} \\times 2^{3}$, $x = 1$")
st.write("예 : $x = 1$, $2^{3} \\times 2^{3} = 2^{4} \\times 2^{2}$")

###1-8
st.markdown("---")

st.header(":school: 1-8")
st.write("👉**문제** : 저장 매체의 용량을 나타내는 단위로 B, KB, MB 등이 있고, 1KB=$2^{10}$B, 1MB=$2^{10}$KB이다. 찬혁이가 컴퓨터로 용량이 36MB인 자료를 내려받으려고 한다. 이 컴퓨터에서 1초당 내려받는 자료의 용량이 $9 \\times{2^{20}}$B일 때, 찬혁이가 자료를 모두 내려받는 데 몇 초가 걸리는지 구하시오.")
st.write("👉**지식요소** : 풀이 방법에 따라 지식 요소 종류 및 순서가 다소 다름")

with st.container():
    st.write("풀이방법1️⃣ 거듭제곱의 곱셈, 거듭제곱의 나눗셈2, 단위의 이해")
    st.write("풀이방법2️⃣ 거듭제곱의 나눗셈1, 수의 나눗셈, 단위의 이해")
    st.write("풀이방법3️⃣ 단위의 이해, 거듭제곱의 나눗셈, 거듭제곱의 나눗셈2")


st.write("👉**모범답안1**")

image_url = 'save/사진자료/1-8 모범답안1.png'
st.image(image_url)

st.write("👉**모범답안2**")

image_url = 'save/사진자료/1-8 모범답안2.png'
st.image(image_url)

st.write("👉**모범답안3**")

image_url = 'save/사진자료/1-8 모범답안3.png'
st.image(image_url)

st.write("✔️문제 풀이 방향이 크게 3가지 종류로 나누어질 수 있음")
st.write("✔️실제로 학생들은 모범답안 1, 2의 방향으로의 풀이가 있고, 모범답안 3의 풀이는 없었음")
st.write("✔️풀이 방법에 따라 평가할 인지 요소의 종류 및 순서가 달라지는데, 이를 하나의 모델에 적용하는 것이 쉽지 않았던 것 같음")

st.write("👉**지식맵**")
image_url = 'save/사진자료/1-8 지식맵.png'
st.image(image_url)

st.write("👉**오개념**")
st.markdown('<span style="color: blue;">1. 등호오류: 서로 다른 식들을 등호로 계속 연결하는 오류</span>', unsafe_allow_html=True)
st.write("예: $2^{10} \\times 2^{10} = {{ 2^{20} \\times 36 } \\over { 2^{20} \\times 9 }}$ = 4초")

st.markdown('<span style="color: blue;">2. 식오류: 논리적으로 맞지 않는 식을 전개하였음. 특정한 부분의 오개념이라기보단 전체적인 식 전개에 오류가 있다고 판단됨</span>', unsafe_allow_html=True)
st.write("예 : $1KB = 2^{10}B , 1MB = 2^{10}KB$ 용량 $36MB$ $1$초당 $9 \\times 2^{20}B$이기에 $(2^{10}KB)^{36} = 2^{360}(K^{36})(B^{36})$, $2^{360}(K^{36})(B^{36}) \\div 9 \\times 2^{20}B = 9 \\times 2^{18}(K^{36})(B^{17})$초")

st.markdown('<span style="color: blue;">3. 단위 혼동: B, KB, MB를 통일하지 않고 혼용해서 사용하는 오류</span>', unsafe_allow_html=True)
st.write("예 : $36MB = 36 \\times 2^{10}KB, 9 \\times 2^{20}KB \\times 4 = 36MB$, $4$초")

st.markdown('<span style="color: blue;">4. 나눗셈 괄호 오류: 나눗셈을 할 때, 분자,분모에 해당하는 식 전체에 괄호를 하지 않는 오류</span>', unsafe_allow_html=True)
st.write("예 : $36MB = 36 \\times 2^{10}KB$,  $36 \\times 2^{10}KB = 36 \\times 2^{10} \\times 2^{10}$B, $36 \\times 2^{10} \\times 2^{10}B = 2^{22} 3^{2}B$ , $2^{22} 3^{2}B \\div 9 \\times 2^{20}B = 2^{2}$, $2^{2} = 4$")

###2-6
st.markdown("---")

st.header(":school: 2-6")
st.write("📖목표가 되는 식을 구하기 위해 등식의 성질을 적절히 사용할 수 있는가?")
st.write("📖단항식의 곱셈과 나눗셈을 할 수 있는가?")

st.write("👉**문제** : $( - 12x^{3}y^{2} ) \\div \\square \\times 18x^{3}y^{3} = 8x^{2}y^{3}$일 때 $\\square$ 안에 알맞은 식을 구하시오.")
st.write("👉**지식요소** : 등식의 성질, 단항식의 곱셈, 단항식의 나눗셈, 거듭제곱의 곱셈, 거듭제곱의 나눗셈")

st.write("👉**모범답안1**")

image_url = 'save/사진자료/2-6 모범답안1.png'
st.image(image_url)


st.write("👉**모범답안2**")

image_url = 'save/사진자료/2-6 모범답안2.png'
st.image(image_url)


st.write("👉**모범답안3**")

image_url = 'save/사진자료/2-6 모범답안3.png'
st.image(image_url)

st.write("👉**모범답안4**")

image_url = 'save/사진자료/2-6 모범답안4.png'
st.image(image_url)

st.write("👉**지식맵**")
image_url = 'save/사진자료/2-6 지식맵.png'
st.image(image_url)

st.write("👉**오개념**")
st.markdown('<span style="color: blue;">1. 역수를 구하는 유형: 단항식의 곱셈과 나눗셈을 할 수 있지만 역수를 구함</span>', unsafe_allow_html=True)
image_url = 'save/사진자료/2-6 오류유형1.png'
st.image(image_url)

st.markdown('<span style="color: blue;">2. 부호 오류: 부호를 잘못 구한 경우</span>', unsafe_allow_html=True)
image_url = 'save/사진자료/2-6 오류유형2.png'
st.image(image_url)

st.markdown('<span style="color: blue;">3. 식을 잘못 본 경우: $18x^{3}y^{3}을 8x^{3}y^{3}$로 잘못보고 계산함</span>', unsafe_allow_html=True)
image_url = 'save/사진자료/2-6 오류유형3.png'
st.image(image_url)

st.markdown('<span style="color: blue;">4. 식의 계산을 할 수 있지만 등식의 성질을 이해하지 못한 경우: 식의 계산에는 오류가 없지만 등식의 성질을 이해하지 못하여 4/9x의 역수를 곱하지 않음</span>', unsafe_allow_html=True)
image_url = 'save/사진자료/2-6 오류유형4.png'
st.image(image_url)

###2-7
st.markdown("---")

st.header(":school: 2-7")
st.write("👉**문제** :  높이가 $(2x)^{2}$인 삼각형의 넓이가 $48x^{3}y^{2}$일 때, 이 삼각형의 밑변의 길이를 구하시오.")
st.write("👉**지식요소** : 곱의 거듭제곱, 거듭제곱의 나눗셈, 다항식의 나눗셈, 삼각형의 넓이")
st.write("👉**피드백 요소** : 미지수의 의미를 명시함, $12xy^2$(삼각형의 넓이공식에서 실수)")

st.write("👉**모범답안1**")
st.write("밑변을 미지수로 놓고 삼각형의 넓이에 대한 식을 세워 계산")
image_url = 'save/사진자료/2-7 모범답안1.png'
st.image(image_url)


st.write("👉**모범답안2**")
st.write("밑변에 대한 식을 세운 후 계산함")
image_url = 'save/사진자료/2-7 모범답안2.png'
st.image(image_url)

st.write("👉**지식맵**")
image_url = 'save/사진자료/2-7 지식맵.png'
st.image(image_url)

st.write("👉**오개념 및 오류**")
st.markdown('<span style="color: blue;">1. 삼각형의 넓이 공식 오류: 삼각형의 넓이 공식에서 2를 나누어야하는데 이를 생략하거나 2를 곱하는 등의 오류를 보임</span>', unsafe_allow_html=True)
image_url = 'save/사진자료/2-7 오개념 및 오류1.png'
st.image(image_url)

st.markdown('<span style="color: blue;">2. 계산 실수: 단순 계산 실수를 한 것으로 보임</span>', unsafe_allow_html=True)
image_url = 'save/사진자료/2-7 오개념 및 오류2.png'
st.image(image_url)


st.markdown('<span style="color: blue;">3. 문제 파악 오류: 문제 파악을 제대로 하지 못함</span>', unsafe_allow_html=True)
image_url = 'save/사진자료/2-7 오개념 및 오류3.png'
st.image(image_url)

###3-3
st.markdown("---")

st.header(":school: 3-3")
st.write("👉**문제** : $A \\div \\frac{3y}{2} = 4x^{2}y + 2xy + 6$일 때. 다항식 A를 구하시오.")
st.write("👉**지식요소** : 등식의 성질, 다항식과 단항식의 곱셈, 단항식의 곱셈, 다항식과 단항식의 나눗셈, 단항식의 나눗셈")

st.write("👉**모범답안1**")
st.write("양변에 $\\frac{3y}{2}$ 를 곱하여 곱셈으로 풀이")
image_url = 'save/사진자료/3-3 모범답안1.png'
st.image(image_url)

st.write("👉**모범답안2**")
st.write("나눗셈을 고치지 않고 다항식과 단항식의 나눗셈으로 풀이")
image_url = 'save/사진자료/3-3 모범답안2.png'
st.image(image_url)

st.write("👉**모범답안3**")
st.write("나눗셈을 역수의 곱셈으로 바꾸어 풀이")
image_url = 'save/사진자료/3-3 모범답안3.png'
st.image(image_url)


st.write("👉**지식맵**")
st.image("images/3_3_km.png")

st.write("👉**오개념**")
st.markdown('<span style="color: blue;">1. 등호 사용의 오류</span>', unsafe_allow_html=True)
st.write("예 : $A \\div \\frac{3y}{2} = 4x^{2}y + 2xy + 6= (4x^{2}y + 2xy + 6) \\times \\frac{3y}{2}$")
st.write("예 : $A \\div \\frac{3y}{2} = 4x^2y + 2xy + 6 =  6x^{2}y^{2} + 3xy^{2} + 9y$")