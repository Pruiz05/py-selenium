import booking.constants as const
import os
from selenium import webdriver

from booking.booking_filtration import BookingFiltration

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

    def change_language(self, language=None):
        language_element = self.find_element_by_css_selector(
            'button[data-tooltip-text="Elegir el idioma que prefieres"]'
        )
        language_element.click()
        selected_language_element = self.find_element_by_css_selector(
            f'a[data-lang="{language}"]'
        )
        selected_language_element.click()

    def select_place_to_go(self, place_to_go):
        searc_field = self.find_element_by_id('ss')
        searc_field.clear()
        searc_field.send_keys(place_to_go)

        fist_result = self.find_element_by_css_selector(
            'li[data-i="0"]'
        )

        fist_result.click()

    def select_dates(self, check_in_date, check_out_date):
        check_in_element = self.find_element_by_css_selector(
            f'td[data-date="{check_in_date}"]'
        )
        check_in_element.click()

        check_out_element = self.find_element_by_css_selector(
            f'td[data-date="{check_out_date}"]'
        )
        check_out_element.click()

    def select_adults(self, count=1):
        selection_element = self.find_element_by_id('xp__guests__toggle')
        selection_element.click()

        while True:
            btn_decrease_adults = self.find_element_by_css_selector(
                'button[aria-label="Decrease number of Adults"]'
            )
            btn_decrease_adults.click()

            adults_value_element = self.find_element_by_id('group_adults')
            adults_value = adults_value_element.get_attribute(
                'value'
            ) # should give back adults count
            if int(adults_value) == 1:
                break

        increase_btn_element = self.find_element_by_css_selector(
            'button[aria-label="Increase number of Adults"]'
        )

        for _ in range(count - 1):
            increase_btn_element.click()

    def click_search(self):
        btn_search = self.find_element_by_css_selector(
            'button[type="submit"]'
        )
        btn_search.click()

    def apply_filtration(self):
        filtration = BookingFiltration(driver=self)
        filtration.apply_star_rating(5)
