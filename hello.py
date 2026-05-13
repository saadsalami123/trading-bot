import requests
import time

TOKEN = "8226890391:AAEBXb6QneQWBHruKvvDvLodiW4Cn12Ussg"
CHAT_ID = "7988390654"

def send_message(text):
    try:
        url = "https://api.telegram.org/bot" + TOKEN + "/sendMessage"
        requests.post(url, data={"chat_id": CHAT_ID, "text": text})
    except:
        print("connection error, retrying...")

def get_price(symbol):
    url = "https://api.binance.com/api/v3/ticker/price?symbol=" + symbol
    response = requests.get(url)
    data = response.json()
    return float(data["price"])

buy_price = 80000
stop_loss = 75000
take_profit = 80000

while True:
    btc_price = get_price("BTCUSDT")
    
    if btc_price < stop_loss:
        send_message("⚠️ Stop Loss! Price: " + str(btc_price))
    elif btc_price > take_profit:
        send_message("✅ Take Profit! Price: " + str(btc_price))
    else:
        send_message("⏳ Waiting... Price: " + str(btc_price))
    
    print("Price: " + str(btc_price))
    time.sleep(60)