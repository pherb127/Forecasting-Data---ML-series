import ccxt
import pandas as pd
from datetime import datetime, timedelta


# We initialize the Binance exchange
exchange = ccxt.binance()

# We define the penny cryptocurrencies that interest us and their trading pairs
cryptos = {
    'TRX/USDT': 'TRX',
    'MATIC/USDT': 'MATIC',
    'FTM/USDT': 'FTM'
}

# Define the timeframe and start date
timeframe = '1d'  # Daily data
start_date = '2019-11-04T00:00:00Z'  # We start four years ago from today

# Function to fetch and process data
def fetch_data(symbol, crypto_name, start_date):
    print(f"Fetching data for {crypto_name}...")
    #We convert the time to millisecond
    since = exchange.parse8601(start_date)
    all_data = []
    while since < exchange.milliseconds():
        try:
            data = exchange.fetch_ohlcv(symbol, timeframe=timeframe, since=since, limit=1000)
            if not data:
                break
            all_data.extend(data)
            since = data[-1][0] + 1  # Set since to the last fetched timestamp + 1 ms
        except Exception as e:
            print(f"Error fetching data for {crypto_name}: {e}")
            break
    # Create DataFrame
    df = pd.DataFrame(all_data, columns=['timestamp', 'open', 'high', 'low', 'close', 'volume'])
    df['timestamp'] = pd.to_datetime(df['timestamp'], unit='ms')
    df.set_index('timestamp', inplace=True)
    df.to_csv(f'{crypto_name}_historical_data.csv')
    print(f"Data for {crypto_name} saved to {crypto_name}_historical_data.csv")

# Fetch data for each cryptocurrency
for symbol, crypto_name in cryptos.items():
    fetch_data(symbol, crypto_name, start_date)

