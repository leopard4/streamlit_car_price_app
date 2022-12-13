import streamlit as st
import numpy as np
import joblib

def run_ml_app() : 
    st.subheader('자동차 금액 예측')

    # 성별은 여자이고, 나이는 50이며, 연봉은 4만달러, 카드빚 5만달러,
    # 자산 20만 달러이면, 이 사람은 얼마짜리 차를 살 것인가 ?
    
    # 성별, 나이, 연봉, 카드빚, 자산을 유저한테 모두 입력받아서
    # 자동차 구매 금액 예측하세요.
   
    gender = st.radio('성별을 선택하세요',['남자','여자'])
    if gender == '남자' :
        gender = 1
    else:
        gender = 0

    age = st.number_input('나이를 입력하세요', 0,100,step=1)
    salary = st.number_input('연봉을 입력하세요', 0, 1000000,step=1000)
    debt = st.number_input('카드빚을 입력하세요', 0, 100000, step=1000)
    worth = st.number_input('자산을 입력하세요',0, 10000000, step=1000)
    
    new_data = np.array([gender,age,salary,debt,worth])
    
    new_data = new_data.reshape(1,5)
    
    regressor = joblib.load('regressor.pkl')    

    y_pred = regressor.predict(new_data)

    if  y_pred < 0 :
        st.info('입력한 데이터로는 금액을 예측하기 어렵습니다.')
    else:
        st.info(f"예측한 가격은 {int(y_pred)} 달러 입니다.")