from model import *
from transformers import AutoTokenizer
import streamlit as st
import torch
import numpy as np
import tensorflow as tf
import sentencepiece as spm
from tensorflow.keras.preprocessing.sequence import pad_sequences
from sample_answer import *

st.header(":teacher: 피드백 방안 1 : 문항1-7")
st.subheader("피드백 과정")
st.write(":one: 지식요소 모델을 이용하여 학생이 가진 지식요소 분석")
st.write(":two: 학생이 가진 지식요소를 기준으로 피드백 제공")
st.write(":three: 루브릭을 기준으로 단계별 힌트 제공")
st.subheader("문항")
st.markdown("$$ (2^4)^x \\times (2^2)^x=2^3 \\times 2^{3x} $$일 때, 자연수 $$x$$의 값을 구하시오.")

response = st.text_input('답안 :', key='answer_input_1_7')

#모델의 이름 정하기
model_name_1_7 = "1-7_att_sp_140" #모델 이름 넣어주기 확장자는 넣지말기!
#모델에 맞는 hyperparameter 설정
vs = 140 #vocab size
emb = 16 #default 값 지정 안했으면 건드리지 않아도 됨
hidden = 32 #default 값 지정 안했으면 건드리지 않아도 됨
nh = 4 #default 값 지정 안했으면 건드리지 않아도 됨
device = "cpu" #default 값 지정 안했으면 건드리지 않아도 됨
max_len = 100
#output_d 설정
output_d_1_7 = 3 #자기의 모델에 맞는 output_d구하기 (지식요소 개수)
c = cfg(vs=vs, emb=emb, hidden=hidden, nh=nh, device=device)

model_1_7 = ATTModel(output_d_1_7, c) #ATTModel 쓰는경우

model_1_7.load_state_dict(torch.load("./save/"+model_name_1_7+".pt"))

#자신에게 맞는 모델로 부르기
tokenizer_1_7 = AutoTokenizer.from_pretrained("./save/"+model_name_1_7) #sp tokenizer 쓰는 경우


enc = tokenizer_1_7(response)["input_ids"] #sp tokenizer
l = len(enc)
if l < max_len :
    pad = (max_len - l) * [0] + enc
else : pad = enc[l-max_len:]
pad_ten = torch.tensor(pad)
pad_ten = pad_ten.reshape(1,max_len)
y = model_1_7(pad_ten)
label_1_7 = y.squeeze().detach().cpu().numpy().round()

if st.button('👀피드백 받기', key='button1_7_1'):
    
    #output차원에 맞추어 피드백 넣기
    
    st.write(response)
    if len(label_1_7) >= 3:
        if label_1_7[0] == 1 and label_1_7[1] == 1 and label_1_7[2] == 1:
            st.success('거듭제곱의 거듭제곱, 거듭제곱의 곱셈, 일차방정식 풀이를 이해하고 있구나!', icon="✅")   
        elif label_1_7[0] == 1 and label_1_7[1] == 1 and label_1_7[2] == 0:
            st.success('거듭제곱의 거듭제곱, 거듭제곱의 곱셈을 이해하고 있구나! 일차방정식 풀이를 올바르게 적용해서 풀이를 완성해보자!', icon="ℹ️")
        elif label_1_7[0] == 1 and label_1_7[1] == 0 and label_1_7[2] == 0:
            st.success('거듭제곱의 거듭제곱을 이해하고 있구나! 거듭제곱의 곱셈, 일차방정식 풀이를 올바르게 적용해서 풀이를 완성해보자!', icon="ℹ️")
        elif label_1_7[0] == 0 and label_1_7[1] == 1 and label_1_7[2] == 0:
            st.success('거듭제곱의 곱셈을 이해하고 있구나! 거듭제곱의 거듭제곱, 일차방정식 풀이를 올바르게 적용해서 풀이를 완성해보자!', icon="ℹ️")
        elif label_1_7[2] == 0 and label_1_7[2] == 0 and label_1_7[2] == 1:
            st.success('일차방정식 풀이를 이해하고 있구나! 거듭제곱의 거듭제곱, 거듭제곱의 곱셈을 올바르게 적용해서 풀이를 완성해보자!', icon="ℹ️")
        else:
            st.info('거듭제곱의 거듭제곱, 거듭제곱의 곱셈, 일차방정식 풀이를 복습하세요!', icon="⚠️")

if st.button('❓힌트1️⃣', key='button1_7_2'):
    st.write('밑이 2로 같으니, 지수를 정리하세요!')

if st.button('❓힌트2️⃣', key='button1_7_3'):
    st.write('거듭제곱의 거듭제곱을 적용해서 식을 정리하세요!')

if st.button('❓힌트3️⃣', key='button1_7_4'):
    st.write('거듭제곱의 곱셈을 적용해서 식을 정리하세요!')

if st.button('💯모범답안', key='button1_7_5'):
    image_path = "save/1-7 모범답안.png-.png"
    st.image(image_path, caption='1-7모범답안')
