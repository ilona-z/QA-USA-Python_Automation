# Imports
import time
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.expected_conditions import element_to_be_clickable
from selenium.webdriver.support.wait import WebDriverWait

import data
from helpers import retrieve_phone_code

class UrbanRoutesPage:
        # Addresses
    from_field = (By.ID, 'from')
    to_field = (By.ID, 'to')
        # Tariff and call button
    supportive_plan_card = (By.XPATH, "//img[@src='/static/media/kids.27f92282.svg' and @alt='Supportive']")
    active_plan_card = (By.XPATH, '//div[@class="card active"]//div[@class="card-title"]')
    call_taxi_button = (By.XPATH, '//button[contains(text(), "Call a taxi")]')
    selected_plan_locator = (By.CSS_SELECTOR, ".tcard.active .tcard-title")
    select_phone_number_field = (By.CLASS_NAME, 'np-text')
    enter_phone_number_field = (By.ID, 'phone')
    enter_phone_code_field = (By.ID, 'code')
    payment_method_button = (By.CLASS_NAME, 'pp-text')
    add_card_button = (By.XPATH, '//div[contains(text(), "Add card")]')
    enter_card_number_field = (By.ID, 'number')
    enter_card_code_field = (By.XPATH, '//input[@class="card-input" and @id="code"]')
    new_card = (By.XPATH, '//div[contains(text(), "Card")]')
    link_button = (By.XPATH, '//button[contains(text(), "Link")]')
    message_for_driver_field = (By.XPATH, '//input[@class="input" and @id="comment"]')
    order_requirements = (By.CLASS_NAME, 'reqs-head')
    select_blanket_and_handkerchiefs = (By.XPATH, '//*[@id="root"]/div/div[3]/div[3]/div[2]/div[2]/div[4]/div[2]/div[1]/div/div[2]/div/span')
    adding_icecream = (By.CLASS_NAME, 'r-counter-label')
    add_icecream = (By.CLASS_NAME, 'counter-plus')
    search_model = (By.CLASS_NAME, 'smart-button-main')
    blanket_checked = (By.XPATH, '//*[@id="root"]/div/div[3]/div[3]/div[2]/div[2]/div[4]/div[2]/div[1]/div/div[2]/div/input')
    icecream_counter_value = (By.XPATH, '//div[@class="counter-value"]')



    def __init__(self, driver):
        self.driver = driver

    def set_from(self, from_address):
        from_field = self.driver.find_element(*self.from_field)
        from_field.send_keys(from_address)

    def set_to(self, to_address):
        self.driver.find_element(*self.to_field).send_keys(to_address)

    def get_from(self):
        return self.driver.find_element(*self.from_field).get_property('value')

    def get_to(self):
        return self.driver.find_element(*self.to_field).get_property('value')

    def click_call_taxi_button(self):
        call_a_taxi_button = self.driver.find_element(*self.call_taxi_button)
        call_a_taxi_button.click()

    def set_route(self, from_address, to_address):
        self.set_from(from_address)
        self.set_to(to_address)
        self.click_call_taxi_button()

    def get_current_selected_plan(self):
        WebDriverWait(self.driver, 5).until(element_to_be_clickable(self.selected_plan_locator))
        plan_element = self.driver.find_element(*self.selected_plan_locator)
        return plan_element.get_property('textContent')

    def select_supportive_plan(self):
        WebDriverWait(self.driver, 5).until(element_to_be_clickable(self.supportive_plan_card))
        supportive_plan_card = self.driver.find_element(*self.supportive_plan_card)
        supportive_plan_card.click()

    def get_phone_number(self):
        return self.driver.find_element(*self.select_phone_number_field).get_attribute('textContent')

    def input_phone_number(self, phone_number):
        self.driver.find_element(*self.select_phone_number_field).click()
        self.driver.find_element(*self.enter_phone_number_field).send_keys(phone_number)
        self.driver.find_element(*self.enter_phone_number_field).send_keys(Keys.RETURN)
        code = retrieve_phone_code(self.driver)
        self.driver.find_element(*self.enter_phone_code_field).send_keys(code)
        self.driver.find_element(*self.enter_phone_code_field).send_keys(Keys.RETURN)

    def get_code(self):
        return self.driver.find_element(*self.enter_phone_code_field).get_attribute('textContent')

    def click_payment_method_button(self):
        time.sleep(2)
        self.driver.find_element(*self.payment_method_button).click()
        self.driver.find_element(*self.add_card_button).click()

    def input_card_number(self, card_number, card_code):
        self.driver.find_element(*self.enter_card_number_field).click()
        self.driver.find_element(*self.enter_card_number_field).send_keys(card_number)
        self.driver.find_element(*self.enter_card_code_field).send_keys(card_code)
        self.driver.find_element(*self.enter_card_code_field).send_keys(Keys.TAB)
        self.driver.find_element(*self.link_button).click()

    def get_new_card_text(self):
        return self.driver.find_element(*self.enter_card_number_field).get_attribute('textContent')

    def get_card_number(self):
        return self.driver.find_element(*self.enter_card_number_field).get_attribute('value')

    def get_card_code(self):
        return self.driver.find_element(*self.enter_card_code_field).get_attribute('textContent')

    def message_driver(self, message_for_driver):
        self.driver.find_element(*self.message_for_driver_field).send_keys(message_for_driver)

    def get_message_for_driver(self):
        time.sleep(2)
        return self.driver.find_element(*self.message_for_driver_field).get_attribute('value')

    def order_blanket_and_handkerchiefs(self):
        self.driver.find_element(*self.select_blanket_and_handkerchiefs).click()

    def get_blanket_checked(self):
        return self.driver.find_element(*self.blanket_checked).get_property('checked')

    def click_add_icecream(self):
        self.driver.find_element(*self.add_icecream).click()

    def get_icecream(self):
        return self.driver.find_element(*self.icecream_counter_value).text

    def select_search(self):
        self.driver.find_element(*self.search_model).click()

    def display_car_model(self):
        return self.driver.find_element(*self.search_model).is_displayed()


















