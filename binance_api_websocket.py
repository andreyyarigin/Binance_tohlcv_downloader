import requests
import json
import pandas as pd

pd.set_option('display.max_rows', 500)
pd.set_option('display.max_columns', 500)
pd.set_option('display.width', 1000)

def binance_api_start_end_time(ticker, interval, starttime, endttime):
    url = 'https://api.binance.com/api/v3/klines?symbol=' + ticker + '&interval=' + interval + '&startTime=' + starttime + '&endTime=' + endttime
    r = requests.get(url)
    data = json.loads(r.content)
    tohlcv = pd.DataFrame(data)
    tohlcv.drop(tohlcv.columns[[6, 7, 8, 9, 10, 11]], axis=1, inplace=True)
    return (tohlcv)


def binance_api_limit(ticker, interval, limit):
    url = 'https://api.binance.com/api/v3/klines?symbol=' + ticker + '&interval=' + interval + '&limit=' + limit
    r = requests.get(url)
    data = json.loads(r.content)
    tohlcv = pd.DataFrame(data)
    tohlcv.drop(tohlcv.columns[[6, 7, 8, 9, 10, 11]], axis=1, inplace=True)
    last_closed_time = int(tohlcv.iloc[0, 0])  # время последней закрытой свечи бинанса
    return (last_closed_time)


# узнаем время последней записанной свечи
with open('/Users/andreyyarigin/PycharmProjects/F_b_s/CSV/btcusdt_5m_lasttime.tmp') as f:
    last_written_time = int(f.readline())  # формат integer

last_closed_time = binance_api_limit('BTCUSDT', '5m', '1') # время последней закрытой свечи
timestamp_interval = 300000  # timestamp 5 min
missed_candles_count = (last_closed_time - last_written_time) / timestamp_interval # количество свечей, которые необходимо загрузить

tohlcv_temp_df = pd.DataFrame() # временный датафрейм, в который будем загружать данные по недостающим свечам

if missed_candles_count > 500:

    requests_count = int(missed_candles_count // 500)
    t1 = last_written_time + timestamp_interval
    for i in range(0, requests_count):
        t2 = t1 + 499 * timestamp_interval
        data_part = binance_api_start_end_time('BTCUSDT', '5m', str(t1), str(t2))
        tohlcv_temp_df = pd.concat([tohlcv_temp_df, data_part], axis=0, names=None)
        t1 = int(tohlcv_temp_df.iloc[-1, 0]) + timestamp_interval

    t1 = t2 + timestamp_interval
    t2 = last_closed_time
    data_part = binance_api_start_end_time('BTCUSDT', '5m', str(t1), str(t2))
    tohlcv_temp_df = pd.concat([tohlcv_temp_df, data_part], axis=0, names=None)
else:
    t1 = last_written_time + timestamp_interval
    t2 = last_closed_time
    data_part = binance_api_start_end_time('BTCUSDT', '5m', str(t1), str(t2))
    tohlcv_temp_df = pd.concat([tohlcv_temp_df, data_part], axis=0, names=None)




