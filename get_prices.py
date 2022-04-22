
import json
from googlefinance import getQuotes
from producer import Producer

PRODUCER = Producer('dog')


class Prices:
    
    def __init__(self) -> None:
        self.tickers = ["EURPLN"]
        
    def get_price(self):
        data = json.dumps(getQuotes('AAPL'), indent=2)
        return data
    
if __name__ == "__main__":
    price = Prices()
    print(price.get_price())