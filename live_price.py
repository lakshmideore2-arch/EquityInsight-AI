import requests
from dotenv import load_dotenv
import os
load_dotenv()
API_KEY = os.getenv("TWELVE_DATA_API_KEY")
def get_live_price(symbol):
    url = (
        f"https://api.twelvedata.com/price"
        f"?symbol={symbol}"
        f"&apikey={API_KEY}"
    )
    response = requests.get(url)
    data = response.json()
    if "price" in data:
        return float(data["price"])
    return None