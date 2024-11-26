class StockWithObserver:
    def __init__(self, name, price):
        self.name = name
        self.price = price
        self.observers = []

    def add_observer(self, observer):
        self.observers.append(observer)

    def remove_observer(self, observer):
        self.observers.remove(observer)

    def set_price(self, price):
        self.price = price
        self.notify_observers()

    def notify_observers(self):
        for observer in self.observers:
            observer.update(self.name, self.price)

class StockObserverWithPattern:
    def __init__(self, name):
        self.name = name

    def update(self, stock_name, new_price):
        print(f"{self.name} notified: {stock_name} price is now ${new_price}")

# Example usage:
stock = StockWithObserver("AAPL", 150)
observer1 = StockObserverWithPattern("Alice")
observer2 = StockObserverWithPattern("Bob")

stock.add_observer(observer1)
stock.add_observer(observer2)

# Price change, observers automatically notified
stock.set_price(160)
