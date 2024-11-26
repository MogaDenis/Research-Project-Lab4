import yfinance as yf
import time
from abc import ABC, abstractmethod
import random

# 1. Observer Pattern Implementation

# Subject Class (Stock Price)
class StockPrice:
    def __init__(self, ticker):
        self.ticker = ticker
        self.price = 0.0
        self.observers = []

    def attach(self, observer):
        self.observers.append(observer)

    def detach(self, observer):
        self.observers.remove(observer)

    def notify(self):
        for observer in self.observers:
            observer.update(self.price)

    def set_price(self, price):
        self.price = price
        self.notify()

    def fetch_new_price(self):
        # Simulate fetching stock price from Yahoo Finance
        stock = yf.Ticker(self.ticker)
        data = stock.history(period="1mo")
        return data['Close'].iloc[-1]  # Get the most recent closing price

# Observer Class (Observer for Stock Price)
class StockObserver(ABC):
    @abstractmethod
    def update(self, price):
        pass

# Concrete Observer (Investor)
class Investor(StockObserver):
    def __init__(self, name):
        self.name = name

    def update(self, price):
        print(f"Investor {self.name} notified: Stock price is now {price:.2f} USD")

# Concrete Observer (Stock Analyst)
class StockAnalyst(StockObserver):
    def __init__(self, name):
        self.name = name

    def update(self, price):
        print(f"Stock Analyst {self.name} notified: Stock price is now {price:.2f} USD")

# 2. Simulate Stock Price Updates and Observers Notifications

def simulate_stock_price_updates(stock):
    # Simulate updating stock price at random intervals
    for _ in range(10):  # Update 10 times
        price = stock.fetch_new_price() + random.uniform(-1.5, 1.5)  # Adding randomness for demonstration
        stock.set_price(price)
        time.sleep(random.randint(1, 5))  # Random wait between updates

# 3. Main Function to Set Up and Run the Experiment
def main():
    # Initialize Stock Price (Subject)
    ticker = "AAPL"  # Apple Inc. as an example
    stock = StockPrice(ticker)
    
    # Initialize Observers
    investor1 = Investor("John Doe")
    investor2 = Investor("Jane Smith")
    analyst1 = StockAnalyst("Alice Cooper")

    # Attach Observers
    stock.attach(investor1)
    stock.attach(investor2)
    stock.attach(analyst1)
    
    # Run the simulation
    print(f"Starting to simulate stock price updates for {ticker}...\n")
    simulate_stock_price_updates(stock)
    print("\nExperiment Completed.")

# 4. Run the Main Function
if __name__ == "__main__":
    main()
