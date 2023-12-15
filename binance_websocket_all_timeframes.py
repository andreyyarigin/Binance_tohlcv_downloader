#!/bin/python3
import websocket
import json
import threading


#keys = ['t', 's', 'i', 'o', 'c', 'h', 'l', 'v']
# s, i были удалены чтобы формат данных подходит к таковому, который загружается из API

keys = ['t', 'o', 'c', 'h', 'l', 'v']

class SocketConn (websocket.WebSocketApp):
    def __init__(self, url):
        super().__init__(url=url, on_open=self.on_open)
        self.on_message = lambda ws, msg: self.message(msg)
        self.on_error = lambda ws, e: print("Error", e)
        self.on_close = lambda ws: print("Closing")

        self.run_forever()

    def on_open(self, ws,):
        #print('Websocket was opened')
        pass

    def message(self, msg):
        msg_dict = json.loads(msg)['k']
        if msg_dict["x"]:
            values = [msg_dict[key] for key in keys]
            print(*values, sep=',', flush=True)

threading.Thread(target=SocketConn, args=('wss://stream.binance.com:443/ws/btcusdt@kline_1m',)).start()
threading.Thread(target=SocketConn, args=('wss://stream.binance.com:443/ws/btcusdt@kline_5m',)).start()
threading.Thread(target=SocketConn, args=('wss://stream.binance.com:443/ws/btcusdt@kline_15m',)).start()
threading.Thread(target=SocketConn, args=('wss://stream.binance.com:443/ws/btcusdt@kline_1h',)).start()
threading.Thread(target=SocketConn, args=('wss://stream.binance.com:443/ws/btcusdt@kline_4h',)).start()
threading.Thread(target=SocketConn, args=('wss://stream.binance.com:443/ws/btcusdt@kline_1d',)).start()