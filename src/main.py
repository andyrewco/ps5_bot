from bot import * 

# for automating the task
import schedule
import time

def main():
    try:
        bot = PS5Bot("https://www.bestbuy.com/site/sony-playstation-5-dualsense-wireless-controller-midnight-black/6464307.p?skuId=6464307", "test", "test")
        status = bot.check_stock()
        price = bot.check_price()
        print(f"DEBUG: in stock? {status}")
    finally:
        bot.cleanup()

main()
