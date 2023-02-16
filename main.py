import os
from Binance_WebSocket import WebSocket
import threading

from coin import Coin


symbol = 'xrpusdt'
percentage = 1
coin = Coin(symbol, percentage)
socket = WebSocket(coin)

t1 = threading.Thread(target=socket.websocket_run, daemon=True)

def f():
  threading.Timer(30.0, f).start()
  if socket.connected:
      # os.system('cls||clear')
      if not coin.work_active:
          socket.websocket_restart()
      #     print('websocket_restart')
      #
      # print('=' * 10)
      # print('work_active: ', coin.work_active)
      # coin.add_bar()
      # print(coin.date)
      # print('last: ',coin.last)
      # print('percent_last_down: ',coin.percent_last_down)
      # print('count bar: ',len(coin.bars))



if __name__ == '__main__':
    f()
    t1.start()
    t1.join()




