class Stock:
    def __init__(self, name, price):
        self.name = name
        self.price = price
        self.observers = []

    def set_price(self, price):
        self.price = price
        for observer in self.observers:
            observer.check_stock()

    def add_observer(self, observer):
        self.observers.append(observer)

    def remove_observer(self, observer):
        self.observers.remove(observer)

class StockObserver:
    def __init__(self, name, stock):
        self.name = name
        self.stock = stock

    def check_stock(self):
        print(f"{self.name} checked: {self.stock.name} price is ${self.stock.price}")

# Example usage:
stock = Stock("AAPL", 150)
observer1 = StockObserver("Alice", stock)
observer2 = StockObserver("Bob", stock)

stock.add_observer(observer1)
stock.add_observer(observer2)

# Price change, observers manually check the stock
stock.set_price(160)
