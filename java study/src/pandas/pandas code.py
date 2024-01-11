!sudo apt-get install -y fonts-nanum
!sudo fc-cache -fv
!rm ~/.cache/matplotlib -rf
#한글폰트 설치

import pandas as pd
import matplotlib.pyplot as plt

plt.rc('font', family='NanumBarunGothic')
plt.rcParams['axes.unicode_minus'] =False

csv_test = pd.read_csv('제주 2019.csv', encoding = 'cp949')

df = pd.DataFrame(csv_test)

#종별로 사고수 그래프로 표현
CountStatus = pd.value_counts(df['종명'].values, sort=True)
CountStatus.plot.bar()
CountStatus.plot.bar(grid=True, figsize=(7,5), fontsize=8)  # figsize, fontsize 조정
