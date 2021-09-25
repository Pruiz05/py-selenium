import booking.constants as const
import os
from selenium import webdriver

class Booking(webdriver.Chrome):
    def __init__(self, driver_path=r"C:/SeleniumDrivers", tearDown=False):
        self.driver_path = driver_path
        self.tearDown = tearDown
        os.environ['PATH'] += self.driver_path
        super(Booking, self).__init__()
        # implicitly wait method
        self.implicitly_wait(15)
        self.maximize_window()
        
    def __exit__(self, exc_type, exc_val, exc_tb):
        if self.tearDown:
            self.quit()

    def land_first_page(self):
        self.get(const.BASE_URL)

    def change_currency(self, currency=None):
        currency_element = self.find_element_by_css_selector(
            'button[data-tooltip-text="Elegir tu moneda"]'
        )
        currency_element.click()
        selected_currency_element = self.find_element_by_css_selector(
            f'a[data-modal-header-async-url-param*="selected_currency={currency}"]'
        )
        selected_currency_element.click()
