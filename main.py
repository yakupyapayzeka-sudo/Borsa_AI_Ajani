import yfinance as yf
import pandas_ta as ta
import requests
import os

def main() -> None:
    """Application entry point."""
    print("Hello from Python.")

    # Sadece Telegram Bilgilerinizi Girin
    TELEGRAM_BOT_TOKEN = os.getenv("TELEGRAM_BOT_TOKEN")
    TELEGRAM_CHAT_ID = os.getenv("TELEGRAM_CHAT_ID")

    def telegram_gonder(mesaj):
        url = f"https://api.telegram.org/bot{TELEGRAM_BOT_TOKEN}/sendMessage"
        response = requests.post(url, json={"chat_id": TELEGRAM_CHAT_ID, "text": mesaj})
        print("Telegram yanıtı: ", response.json())

    # BIST'ten veriyi çek
    ticker = yf.Ticker("THYAO.IS")
    df = ticker.history(period="60d", interval="1d")
    df.ta.rsi(length=14, append=True)

    fiyat = df['Close'].iloc[-1]
    rsi = df['RSI_14'].iloc[-1]

    rapor = f"📊 THYAO.IS Güncel Durum:\nFiyat: {fiyat:.2f} TRY\nRSI: {rsi:.2f}"
    telegram_gonder(rapor)
    print("Telegram'a gönderildi!")


if __name__ == "__main__":
    main()

