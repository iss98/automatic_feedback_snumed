from model import *
from transformers import AutoTokenizer
"""
자신의 모델에 맞는 변수 설정해주기
"""
model_name = "3-3_rnn_sp_100" #모델 이름 넣어주기 확장자는 넣지말기!
#모델에 맞는 hyperparameter 설정
vs = 100 #vocab size
emb = 16 #default 값 지정 안했으면 건드리지 않아도 됨
hidden = 32 #default 값 지정 안했으면 건드리지 않아도 됨
nh = 4 #default 값 지정 안했으면 건드리지 않아도 됨
device = "cpu" #default 값 지정 안했으면 건드리지 않아도 됨
#output_d 설정
output_d = 5 #자기의 모델에 맞는 output_d구하기 (지식요소 개수)
c = cfg(vs=vs, emb=emb, hidden=hidden, nh=nh, device=device)


"""
model과 tokneizer 부르기
"""
model = RNNModel(output_d, c)
model.load_state_dict(torch.load("./save/"+model_name+".pt"))
#자신에게 맞는 모델로 부르기
tokenizer = AutoTokenizer.from_pretrained("./save/"+ model_name)