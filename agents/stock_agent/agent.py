# Enhanced Stock Agent with improved comments and structure

from yfinance import Ticker

class StockAgent:
    """Agent to fetch stock data using the Yahoo Finance library."""

    def fetch_stock_data(self, symbol):
        """Fetch stock data for a given symbol.

        Args:
            symbol (str): The stock symbol to fetch data for.

        Returns:
            dict: Stock data including price, currency, market state, and name.
        """
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
        """Process input data to fetch stock information.

        Args:
            input_data (dict): Input data containing the stock symbol.

        Returns:
            dict: The fetched stock data.
        """
        symbol = input_data.get("symbol")
        return self.fetch_stock_data(symbol)
