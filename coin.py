from bar import Bar
from datetime import datetime
import os


class Coin():

    def __init__(self, symbol: str, percentage):
        self.percentage = percentage
        self.alerts_list = []
        self.date = 0
        self.symbol = symbol
        self.bars:list[Bar]  = []
        self.last = 0
        self.percent_last_down  = 0
        self.start = False
        self.alerts_f = True
        self.work_active = False

    def add_bar(self):
        self.work_active = False
        if self.start:
            if len(self.bars) > 59:
                self.bars.pop(0)
            self.bars.append(Bar(self.bars[len(self.bars) - 1].close))

    def add_bar_st(self, symbol, last):
        if self.start == False and self.last != 0:
            if symbol == self.symbol:
                self.bars.append(Bar(last))
                self.start = True

    def trade(self,  symbol, last, date):
        self.work_active = True
        self.date = datetime.fromtimestamp(date/1000)

        self.add_bar_st(symbol, last)

        if symbol == self.symbol:
            self.last =  last
            if self.start:
                 self.bars[len(self.bars) - 1].sort(last)

        self.percent_calculation()

        if len(self.bars) > 2:
             self.alerts()
        # os.system('cls||clear')
        # print(self.bars_btc[len(self.bars_btc) - 1])
        # print(self.bars_eth[len(self.bars_eth) - 1])

    def percent_calculation(self):
        max = 0
        min = 1000000

        for b in self.bars:

            if max < b.high:
                max = b.high

            if min > b.low:
                min = b.low

        if max - self.last > 0:
                 self.percent_last_down = (max - self.last ) / (self.last / 100)
        else:
                self.percent_last_down = 0

    def  alerts(self):
        if self.alerts_f and abs(self.percent_last_down) > self.percentage:
            print('+' * 70)
            print(f"{self.date} alerts: percent_last_down >  {self.percent_last_down}")
            self.alerts_list.append(f"{self.date} alerts: percent_last_down >  {self.percent_last_down}")
            self.alerts_f = False

        if not self.alerts_f and self.percent_last_down < 0.1:
            print('+' * 70)
            print(f"{self.date} alerts: percent_last_down < {self.percent_last_down}")
            self.alerts_f = True