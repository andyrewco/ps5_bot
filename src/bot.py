from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager


class PS5Bot:
    def __init__(self, base_url, contact_info, payment_info):
        # Initiate the browser
        self.browser = webdriver.Chrome(ChromeDriverManager().install())
        self.browser.get(base_url)

        # Instantiate variables
        self.base_url = base_url
        self.contact_info = contact_info
        self.payment_info = payment_info

    def get_base_url(self):
        return self.base_url

    def check_stock(self):
        print(f"LOG: Checking stock...")

        status = self.browser.find_element_by_class_name("add-to-cart-button").text

        if ("add to cart" in status.lower()):
            return True
        else:
            return False

    def check_price(self):
        print(f"LOG: Checking price...")
        raise NotImplementedError

    def run_bot(self):
        print(f"Running bot at {self.base_url}")
        raise NotImplementedError

    def cleanup(self):
        print(f"LOG: Cleaning up the browser")
        self.browser.quit()
