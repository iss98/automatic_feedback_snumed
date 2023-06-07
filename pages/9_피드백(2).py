from model import *
from transformers import AutoTokenizer
import streamlit as st
import torch
import numpy as np
import tensorflow as tf
import sentencepiece as spm
from tensorflow.keras.preprocessing.sequence import pad_sequences
from sample_answer import *

st.header(":teacher: 피드백 방안 2 : 문항2-6")
st.subheader("피드백 과정")
st.write(":one: 지식요소 모델, 오개념 모델을 바탕으로 학생의 지식요소와 오개념 분석")
st.write(":two: 가장 유사한 모범답안 찾기")
st.write(":three: 지식요소, 오개념, 모범답안을 기준으로 다양한 피드백을 생성")
st.write(":four: 유사한 모범답안을 기준으로 학생의 풀이에 부합하는 힌트 제공")
st.subheader("문항")
st.markdown(":blue[$( - 12x^{3}y^{2} ) \div \\square \\times 18x^{3}y^{3} = 8x^{2}y^{3}$]일 때 $\square$ 안에 알맞은 식을 구하시오. ")
response = st.text_input('답안 :', "답안을 작성해주세요")

######자신의 모델에 맞는 변수 설정해주기

model_name = "2-6_att_sp_100" #모델 이름 넣어주기 확장자는 넣지말기!
#모델에 맞는 hyperparameter 설정
vs1 = 100 #vocab size
emb1 = 256 #default 값 지정 안했으면 건드리지 않아도 됨
hidden1 = 32 #default 값 지정 안했으면 건드리지 않아도 됨
nh1 = 4 #default 값 지정 안했으면 건드리지 않아도 됨
device = "cpu" #default 값 지정 안했으면 건드리지 않아도 됨
max_len = 100
#output_d 설정
output_d1 = 5 #자기의 모델에 맞는 output_d구하기 (지식요소 개수)
c = cfg(vs=vs1, emb=emb1, hidden=hidden1, nh=nh1, device=device)

model = ATTModel(output_d1, c) #ATTModel 쓰는경우

model.load_state_dict(torch.load("./save/"+model_name+".pt"))

######자신에게 맞는 모델로 부르기
tokenizer = AutoTokenizer.from_pretrained("./save/"+ model_name) #sp tokenizer 쓰는 경우

######자동 채점해주는 코드

enc = tokenizer(response)["input_ids"] #sp tokenizer
l = len(enc)
if l < max_len :
    pad = (max_len - l) * [0] + enc
else : pad = enc[l-max_len:]
pad_ten = torch.tensor(pad)
pad_ten = pad_ten.reshape(1,max_len)
y = model(pad_ten)
label = y.squeeze().detach().cpu().numpy().round()
print("label_kc :",label)

######유사한 모범답안

model1 = tf.keras.models.load_model('./save/lstm_class.h5')
sp1 = spm.SentencePieceProcessor(model_file='./save/2-7_class_v.model')
sequences1 = [sp1.encode_as_ids(response)]
X1 = pad_sequences(sequences1, maxlen=128)
pred1 = model1.predict(X1 .reshape(1,128))
k=np.argmax(pred1)


######정오답

model2 = tf.keras.models.load_model('./save/lstm_corr.h5')
sp2 = spm.SentencePieceProcessor(model_file='./save/2-7_cor_v.model')
sequences2 = [sp2.encode_as_ids(response)]
X2 = pad_sequences(sequences2, maxlen=150)
corr = model2.predict(X2 .reshape(1,150))

######오류유형
model_name_mc="2-6_mc_att_sp_100"
model_mc = ATTModel(5, c) 
model_mc.load_state_dict(torch.load("./save/"+model_name_mc+".pt"))
tokenizer_mc = AutoTokenizer.from_pretrained("./save/"+ model_name_mc)
enc_mc = tokenizer_mc(response)["input_ids"] #sp tokenizer
l = len(enc_mc)
if l < max_len :
    pad_mc = (max_len - l) * [0] + enc_mc
else : pad_mc = enc_mc[l-max_len:]
pad_ten_mc = torch.tensor(pad_mc)
pad_ten_mc = pad_ten_mc.reshape(1,max_len)
y_mc = model_mc(pad_ten_mc)
label_mc = y_mc.squeeze().detach().cpu().numpy().round()
print("label_mc :", label_mc)

######인지요소

g=[]
b=[]
if k!=4:
    (g if label[0] == 1 else b).append('등식의 성질')    
(g if label[1] == 1 else b).append('단항식의 곱셈')
(g if label[2] == 1 else b).append('단항식의 나눗셈')
(g if label[3] == 1 else b).append('거듭제곱의 곱셈')
(g if label[4] == 1 else b).append('거듭제곱의 나눗셈')
g_str = ' , '.join(g)
b_str = ' , '.join(b)

#####피드백받기

if st.button('👀피드백 받기'):
    #output차원에 맞추어 피드백 넣기
    
    st.write(response)
    
    if corr[0].round() == 1 and len(response)>30:
        st.success(f'정답입니다! {g_str} 을 이해하고 있네요 ', icon="✅")
    elif corr[0].round() == 1 and len(response)<=30 :
        st.success(f'정답입니다! {g_str} 을 이해하고 있네요. 하지만 풀이과정을 좀 더 자세히 써주세요', icon="✅")
    elif corr[0].round() == 0 and len(b)>0 and len(g)>0:
        st.info(f'다시 한 번 풀어볼까요? {g_str} 을 이해하고 있네요. 하지만 계산 과정과 {b_str} 과정을 검토해봅시다.', icon="ℹ️")
    elif corr[0].round() == 0 and len(b)>0 and len(g)==0:
        st.info(f'다시 한 번 풀어볼까요? 계산 과정과 {b_str} 과정을 검토해봅시다.', icon="ℹ️")
    elif corr[0].round() == 0 and len(b)==0 and len(g)>0:
        st.info(f'다시 한 번 풀어볼까요? {g_str} 을 이해하고 있네요. 하지만 실수한 것이 있는지 한번 검토해봅시다.', icon="ℹ️")
    if corr[0].round() == 0 and label_mc[1]==1:
        st.write(f'혹시 구한 것이 $\square$의 역수가 아닌가요?', icon="ℹ️")
    if corr[0].round() == 0 and label_mc[2]==1:
        st.write(f'혹시 부호를 잘못 구하진 않았나요?', icon="ℹ️")
    if corr[0].round() == 0 and label_mc[3]==1:
        st.write(f'혹시 식을 잘못 보고 쓰지 않았나요?', icon="ℹ️")
    if corr[0].round() == 0 and label_mc[4]==1:
        st.write(f'계산은 모두 맞게 했지만 등식의 성질을 잘못 이용하진 않았나요?', icon="ℹ️")
        
        
#####힌트받기
      
if "hint" not in st.session_state:
    st.session_state["hint"] = 0

if st.button("❓힌트 받기"):
    st.session_state["hint"] = st.session_state["hint"]+1
    
    if label[0] == 0 and k!=4:
        st.info('등식의 성질에 의해 양변에 같은 항을 곱하거나 나눌 수 있습니다. 예를 들어', icon="ℹ️")
        st.latex('\square \\times 2x = 4x')
        st.latex('\square \\times 2x \\times \\frac{1}{2x}= 4x \\times \\frac{1}{2x}')
        st.latex('\square = 4x \\times \\frac{1}{2x} = 2')
    if label[3] == 0:
        st.info('밑이 같은 거듭제곱의 곱셈은 지수끼리 더합니다. 예를 들어', icon="ℹ️")
        st.latex('x^{2} \\times x^{3} = x^{2+3}=x^{5}')     
    if label[1] == 0:
        st.info('단항식의 곱셈은 숫자끼리, 문자는 같은 문자끼리 곱합니다. 예를 들어', icon="ℹ️")
        st.latex('2xy \\times 3xy^{2} = 2 \\times 3 \\times x \\times x \\times y^{2} = 6x^{2}y^{3}') 
    if label[4] == 0:
        st.info('밑이 같은 거듭제곱의 나눗셈은 지수의 차를 이용합니다. 예를 들어', icon="ℹ️")
        st.latex('x^{5} \\times \\frac{1}{x^{2}} =x^{5-2}=x^{3}')
        st.latex('x^{2} \\times \\frac{1}{x^{4}} = \\frac{1}{x^{4-2}}=\\frac{1}{x^{2}}')  
    if label[2] == 0:
        st.info('단항식의 나눗셈은 역수를 이용하여 곱셈으로 바꿔 계산합니다. 예를 들어', icon="ℹ️")
        st.latex('6x^{2}y^{3} \\div 3xy = 6x^{2}y^{3} \\times \\frac{1}{3xy}')
        st.latex(' = 6 \\times \\frac{1}{3} \\times x^{2} \\times \\frac{1}{x} \\times y^{3}\\times \\frac{1}{y^{2}} = 2xy^{2}') 
    if label[0]==1 and label[1]==1 and label[2]==1 and label[3]==1 and label[4]==1:
        st.info('식의 계산을 잘 이해하고 있어 받을 힌트가 없네요. 실수한 것이 있는지 한번 검토해봅시다. ', icon="ℹ️")
            
            
if st.session_state["hint"]>0:
    if st.button("❓힌트 더 받기"):
        
        if k==1:
            if label[0] == 0:
                st.info('등식의 성질에 의해 양변에 같은 항을 곱하거나 나누면', icon="ℹ️")
                st.latex(lst1[1])
                st.latex(lst1[2])
            if label[1] == 0 or label[2] == 0:
                st.info('단항식의 곱셈과 나눗셈은 계수는 계수끼리, 문자는 문자끼리 계산합니다', icon="ℹ️")
                st.latex(lst1[2])
                st.latex(lst1[3])
            if label[3] == 0 or label[4] == 0:
                st.info('밑이 같은 거듭제곱의 곱셈은 지수의 합, 나눗셈은 지수의 차를 이용합니다', icon="ℹ️")
                st.latex(lst1[3])
                st.latex(lst1[4])
        if k==2:
            if label[2] == 0:
                st.info('단항식의 나눗셈은 계수는 계수끼리, 문자는 문자끼리 계산합니다', icon="ℹ️")
                st.latex(lst2[1])
            if label[4] == 0:
                st.info('밑이 같은 거듭제곱의 나눗셈은 지수의 차를 이용합니다', icon="ℹ️")
                st.latex('\\frac{8}{18} \\times x^{2} \\times \\frac{1}{x^{3}} \\times \\frac{y^{3}}{y^{3}}=\\frac{4}{9x}')
            if label[0] == 0:
                st.info('등식의 성질에 의해 양변에 같은 항을 곱하거나 나누면', icon="ℹ️")
                st.latex(lst2[2])
                st.latex('\square = (- 12x^{3}y^{2}) \div \\frac{4}{9x}')
            if label[1] == 0:
                st.info('단항식의 곱은 계수는 계수끼리, 문자는 문자끼리 계산합니다', icon="ℹ️")
                st.latex(' \square = (- 12x^{3}y^{2}) \div \\frac{4}{9x} = (- 12x^{3}y^{2}) \\times \\frac{9x}{4}' )
                st.latex(' \square = -12 \\times \\frac{9}{4} \\times x^{3} \\times x \\times y^{2}')
            if label[3] == 0:
                st.info('밑이 같은 거듭제곱의 곱셈은 지수의 합를 이용합니다', icon="ℹ️")
                st.latex(' \square = -12 \\times \\frac{9}{4} \\times x^{3} \\times x \\times y^{2}')            
                st.latex(' \square = - 27x^{4}y^{2} ') 
        if k==3:
            if label[1] == 0:
                st.info('단항식의 곱셈은 계수는 계수끼리, 문자는 문자끼리 계산합니다', icon="ℹ️")
                st.latex(lst3[1])
                st.latex(lst3[2])
            if label[3] == 0:
                st.info('밑이 같은 거듭제곱의 곱셈은 지수의 합를 이용합니다', icon="ℹ️")
                st.latex(lst3[2])
                st.latex(lst3[3]) 
            if label[0] == 0:
                st.info('등식의 성질에 의해 양변에 같은 항을 곱하거나 나누면', icon="ℹ️")
                st.latex(lst3[3])
                st.latex(lst3[4])
            if label[2] == 0:
                st.info('단항식의 나눗셈은 계수는 계수끼리, 문자는 문자끼리 계산합니다', icon="ℹ️")
                st.latex(lst3[4])
                st.latex(' \square =  -216 \div  8 \\times x^{6} \div x^{2} \\times y^{5} \div y^{3}')
            if label[4] == 0:
                st.info('밑이 같은 거듭제곱의 나눗셈은 지수의 차를 이용합니다', icon="ℹ️")
                st.latex(lst3[6])
        if k==4:
            st.latex(lst4[0])
            if label[1] == 0 or label[2] == 0:
                st.info('단항식의 곱셈과 나눗셈은 계수는 계수끼리, 문자는 문자끼리 계산합니다', icon="ℹ️")
                st.latex(lst4[1])
                st.latex('x^{3} \\times x^{3} \div x^{a} = x^{2}' )
                st.latex('y^{2} \\times y^{3} \div y^{b} = y^{3}')
            if label[3] == 0 or label[4] == 0:
                st.info('밑이 같은 거듭제곱의 곱셈은 지수의 합, 나눗셈은 지수의 차를 이용합니다', icon="ℹ️")
                st.latex(lst4[2])
                st.latex(lst4[3]) 
           
           

if st.button('💯풀이보기'):
    if k==1:
        for i in range(len(lst1)):
            st.latex(lst1[i])
    if k==2:
        for i in range(len(lst2)):
            st.latex(lst2[i])
    if k==3:
        for i in range(len(lst3)):
            st.latex(lst3[i])
    if k==4:
        for i in range(len(lst4)):
            st.latex(lst4[i])