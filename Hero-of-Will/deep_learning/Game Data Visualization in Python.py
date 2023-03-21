import pandas as pd
import matplotlib.pyplot as plt

# 데이터 불러오기'
# data = pd.read_csv('game_data_JiSung - 시트1.csv')
data = pd.read_csv('data.csv')

# score 컬럼 시각화
plt.bar(range(len(data)), data['score'])
plt.title('Score')
plt.xlabel('Data Index')
plt.ylabel('Score')
plt.show()

# time 컬럼 시각화
plt.bar(range(len(data)), data['time'])
plt.title('Time')
plt.xlabel('Data Index')
plt.ylabel('Time')
plt.show()

# maxcombo 컬럼 시각화
plt.bar(range(len(data)), data['maxcombo'])
plt.title('Max Combo')
plt.xlabel('Data Index')
plt.ylabel('Max Combo')
plt.show()

# coin 컬럼 시각화
plt.bar(range(len(data)), data['coin'])
plt.title('Coin')
plt.xlabel('Data Index')
plt.ylabel('Coin')
plt.show()

# item 컬럼 시각화
item_list = list(set(data['item']))

# 각 item이 등장하는 횟수 세기
counts = [sum(data['item'] == item) for item in item_list]

# 바 차트 그리기
plt.bar(item_list, counts)
plt.xlabel('Item')
plt.ylabel('Count')
plt.title('Count by Item')
plt.show()