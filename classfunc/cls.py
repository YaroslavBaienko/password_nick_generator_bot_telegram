class Accaunt:
    def __init__(self, bought=0.00, sold=0.00, buy_goods=list(), sell_goods=list(), amount=0.0, currency='UAH'):
        self.amount = amount
        self.currency = currency
        self.buy_goods = buy_goods
        self.sell_goods = sell_goods
        self.bought = bought
        self.sold = sold

    def buy(self, cost: float, good: str):
        self.amount = self.amount - cost
        self.buy_goods.append(good)
        self.bought = self.bought + cost

    def sell(self, cost: float, good: str):
        self.amount = self.amount + cost
        self.sell_goods.append(good)
        self.sold = self.sold + cost

class Premium(Accaunt):
    def __init__(self, bought=0.00, sold=0.00, buy_goods=list(), sell_goods=list(), amount=0.0, currency='UAH', discount=0.00):
        self.discount = discount
        super().__init__(bought=0.00, sold=0.00, buy_goods=list(), sell_goods=list(), amount=0.0, currency='UAH')

    def buy(self, cost: float, good: str):
        self.amount = self.amount - cost * self.discount
        self.buy_goods.append(good)
        self.bought = self.bought + cost

    def sell(self, cost: float, good: str):
        self.amount = self.amount + cost * self.discount
        self.sell_goods.append(good)
        self.sold = self.sold + cost
