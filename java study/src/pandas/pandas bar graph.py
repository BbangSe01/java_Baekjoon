import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

csv_test = pd.read_csv('로드킬 저감대책 csv~.csv', encoding = 'cp949')

df = pd.DataFrame(csv_test)
df['주소'].str.split(" ", expand=True)
df['도'] = df['주소'].str.split(" ",expand=True)[0] #'도'를 기준으로 묶기 위한 작업

df.groupby('도').sum()

# 그림 사이즈, 바 굵기 조정
fig, ax = plt.subplots(figsize=(9,7))
bar_width = 0.25

# 도가 9개이므로
index = np.arange(9)

# 각 연도별로 2개 로드길 발생건수를 순서대로 나타내는 과정
b1 = plt.bar(index, df.groupby('도').sum()['로드킬 발생건수(건)-2019'], bar_width, alpha=0.4, color='red', label='로드킬 발생건수(건)-2019')

b2 = plt.bar(index + bar_width, df.groupby('도').sum()['로드킬 발생건수(건)-2021'], bar_width, alpha=0.4, color='blue', label='로드킬 발생건수(건)-2021')


# x축 위치를 정 가운데로 조정하고 x축의 텍스트를 year 정보와 매칭
plt.xticks(np.arange(9), labels=['강원도', '경기도', '경상남도', '경상북도', '세종특별자치시', '전라남도', '전라북도', '충청남도', '충청북도'], size = 8)

# x축, y축 이름 및 범례 설정
plt.ylabel('로드킬 발생건수', size = 10)
plt.legend()
plt.show()