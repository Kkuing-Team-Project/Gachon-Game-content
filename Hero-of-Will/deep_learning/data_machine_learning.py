import pandas as pd
import numpy as np
import warnings
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression

# 경고 메시지 무시
warnings.filterwarnings('ignore', message='scipy._lib.messagestream.MessageStream size changed*')

# 데이터 불러오기
data = pd.read_csv('../deep_learning/game_data - 시트1.csv')

# 아이템 리스트 생성
item_list = ['창', '로켓', '표창', '대포', '나팔총', '플레일', '해머', '소드', '폭탄', '도끼', '투창', '캐논']

# 아이템 인덱스로 변경
for i, row in data.iterrows():
    if row['item'] in item_list:
        data.at[i, 'item'] = item_list.index(row['item'])
    else:
        data.at[i, 'item'] = np.nan

# feature 선택
features = ['score', 'time', 'maxcombo', 'coin', 'item']

# 데이터 나누기
X = data[features].iloc[:-1]
y = data[features].iloc[1:]

max_x_score, max_y_score, min_x_score, min_y_score = max(X['score']), max(y['score']), min(X['score']), min(y['score'])
max_x_time, max_y_time, min_x_time, min_y_time = max(X['time']), max(y['time']), min(X['time']), min(y['time'])
max_x_maxcombo, max_y_maxcombo, min_x_maxcombo, min_y_maxcombo = max(X['maxcombo']), max(y['maxcombo']), min(X['maxcombo']), min(y['maxcombo'])
max_x_coin, max_y_coin, min_x_coin, min_y_coin = max(X['coin']), max(y['coin']), min(X['coin']), min(y['coin'])

max_score, min_score = max(max_x_score, max_y_score), min(min_x_score, min_y_score)
max_time, min_time = max(max_x_time, max_y_time), min(min_x_time, min_y_time)
max_maxcombo, min_maxcombo = max(max_x_maxcombo, max_y_maxcombo), min(min_x_maxcombo, min_y_maxcombo)
max_coin, min_coin = max(max_x_coin, max_y_coin), min(min_x_coin, min_y_coin)

# 학습 데이터와 테스트 데이터로 나누기
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=0)

# 모델 생성 및 학습
regressor = LinearRegression()
regressor.fit(X_train, y_train)

# 새로운 데이터 생성
# new_data = pd.DataFrame({'score': [44], 'time': [12], 'maxcombo': [5], 'coin': [60], 'item': ['캐논']})
new_data = pd.DataFrame({
    'score': np.random.randint(low=0, high=max_score, size=10000),
    'time': np.random.randint(low=0, high=max_time, size=10000),
    'maxcombo': np.random.randint(low=0, high=max_maxcombo, size=10000),
    'coin': np.random.randint(low=0, high=max_coin, size=10000),
    'item': np.random.choice(['창', '로켓', '표창', '대포', '나팔총', '플레일', '해머', '소드', '폭탄', '도끼', '투창', '캐논'], size=10000)
}).copy()

# 새로운 데이터 아이템 인덱스로 변경
new_data['item'] = new_data['item'].apply(lambda x: item_list.index(x) if x in item_list else len(item_list))

# 새로운 데이터 예측 수행
new_pred = regressor.predict(new_data)

# 예측 결과 출력
print('의지의 히어로%')
print('score:', int(new_pred[0][0]))
print('time:', int(new_pred[0][1]))
print('maxcombo:', int(new_pred[0][2]))
print('coin:', int(new_pred[0][3]))

if new_pred[0][4] >= len(item_list):

    print('item: Unknown')
else:
    print('item:', item_list[int(new_pred[0][4])])
