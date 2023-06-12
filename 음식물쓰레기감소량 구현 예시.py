'''하루에 준비하는 중식 기준량을 1400인분으로 잡았을 땨
1인 한 끼 음식물 쓰레기량 평균:  0.09kg
음식물 1kg 당 배출되는 온실가스  대략:1.65kg
탄소 1kg를 없애기 위해 탄소흡수를 해야 하는 하루 소나무 수: 73

절약한 음식물 배출량 = (1300인(중식 기준 인원, 임의) – 예측 인원) * 0.09kg
절약한 탄소배출량 = 절약한 음식물 배출량 * 1.65kg
소나무 몇 그루가 쉴 수 있는지 = 절약한 탄소 배출량(kg) * 73
위 기준을 이용하여 간단한 웹을 구현하여 예측 결과를 바탕으로 음식물 쓰레기가 얼마나 줄었는지 시각화
'''
import streamlit as st
from PIL import Image
import pandas as pd
df = pd.read_csv('C:/Users/kjh25/example/Lib/site-packages/streamlit/ST_AIS_DEMO/pages/sub_xgb.csv')

df['기본량'] = 1300
df['중식폐기인분'] = df['기본량'] - df['중식계'] 
df['중식 음식물 쓰레기(kg)'] = df['중식폐기인분'] * 0.09

def food_waste(날짜):
    x =  df.loc[df['일자'] == 날짜, '중식 음식물 쓰레기(kg)']
    return int(x) 

st.title('오늘의 환경 보호🌳')
a = st.text_input('원하는 날짜를 입력하세요"Y-m-d"')
st.markdown('### 오늘 줄인 음식물 쓰레기: {}kg'.format(food_waste(a)))
st.markdown('## 🚗오늘 줄인 탄소배출량: {}kg🚗'.format(food_waste(a)*1.65))


def main() :
    
    img = Image.open('C:/Users/kjh25/OneDrive/사진/christmas-tree-g21b1441a1_1280.png')
    img = img.resize((int(img.width / 2), int(img.height / 2)))
    st.image(img)

if __name__ == "__main__" :
    main()

st.markdown('# X {}'.format(int(food_waste(a)*1.65*73)))
st.markdown('🌳침엽수 {}그루가 하루동안 흡수해야하는 탄소량을 줄였습니다🌳'.format(int(food_waste(a)*1.65*73)))