# преобразует CSV с полными историческими данными в CSV, куда можно добавлять данные из Binance API и Binance Websocket
# (сокращает количество столбцов до Time, O, H, L, C, Volume)

import pandas as pd
pd.set_option('display.max_rows', 500)
pd.set_option('display.max_columns', 500)
pd.set_option('display.width', 1000)

df = pd.read_csv('/Users/andreyyarigin/PycharmProjects/F_b_s/CSV/btcusdt_result.csv', header=None) # загружаем файл с полными историческими данными
df.drop([6,7,8,9,10,11], axis=1, inplace=True) #оставляем только нужные колонки open time (timestampt, onen, high, low, close, volume)
df.to_csv ('/Users/andreyyarigin/PycharmProjects/F_b_s/CSV/btcusdt_5m_tohlcv.csv', header=None, index=None) # записываем видоизмененный CSV (tohlcv)

# далее записываем время последней свечи во временный файл
last_time=df.iloc[-1,0]
f = open('/Users/andreyyarigin/PycharmProjects/F_b_s/CSV/btcusdt_5m_lasttime.tmp','w')  # w : writing mode  /  r : reading mode  /  a  :  appending mode
f.write('{}'.format(last_time))
f.close()

# Релизовать универсальность скрипта