import streamlit as st


def run_home_app() : 
    st.text('이 앱은 고객 데이터와 자동차 구매 데이터에 대한 내용입니다. ')
    st.text('데이터 분석 및 고객 정보를 넣으면, 얼마정도의 차를 구매할지를 예측해 봅니다.')
    img_url = 'http://img.danawa.com/images/mobile/MDNW/mainContent/219/21929.jpg?ver=20221201102335'
    st.image(img_url)