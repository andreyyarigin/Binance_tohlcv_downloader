import requests
import json
import pandas as pd

pd.set_option('display.max_rows', 500)
pd.set_option('display.max_columns', 500)
pd.set_option('display.width', 1000)

# узнаем время последней записанной свечи
with open('/Users/andreyyarigin/PycharmProjects/F_b_s/CSV/btcusdt_5m_lasttime.tmp') as f:
    last_time = int(f.readline()) # формат integer

url = 'https://api.binance.com/api/v3/klines?symbol=BTCUSDT&interval=5m&limit=1'
r = requests.get(url)
data = json.loads(r.content)
data1 = pd.DataFrame(data)
data1.drop(data1.columns[[6,7,8,9,10,11]], axis=1, inplace=True)
last_closed_time = int(data1.iloc[0,0]) #время последней закрытой свечи бинанса

print(last_time)
print(last_closed_time)
print ((last_closed_time-last_time)/300000)

# далее тесты

url = 'https://api.binance.com/api/v3/klines?symbol=BTCUSDT&interval=5m&startTime=1702541400000&endTime=1702541700000'
r = requests.get(url)
data = json.loads(r.content)
data1 = pd.DataFrame(data)
data1.drop(data1.columns[[6,7,8,9,10,11]], axis=1, inplace=True)
print (data1)


