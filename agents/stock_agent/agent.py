# Agent logic for fetching stock data using Yahoo Finance library

from yfinance import Ticker

class StockAgent:
    def fetch_stock_data(self, symbol):
        try:
            stock = Ticker(symbol)
            stock_info = stock.info
            return {
                "symbol": symbol,
                "price": stock_info.get("regularMarketPrice"),
                "currency": stock_info.get("currency"),
                "marketState": stock_info.get("marketState"),
                "name": stock_info.get("shortName")
            }
        except Exception as e:
            return {"error": str(e)}

    def process(self, input_data):
        symbol = input_data.get("symbol")
        return self.fetch_stock_data(symbol)
