from selenium.webdriver.common.by import By
from pages.base_page import BasePage


class InventoryPage(BasePage):
    PAGE_TITLE = (By.CLASS_NAME, "title")
    ADD_TO_CART_BUTTONS = (By.CSS_SELECTOR, "[data-test^='add-to-cart']")
    CART_BADGE = (By.CLASS_NAME, "shopping_cart_badge")
    CART_ICON = (By.CLASS_NAME, "shopping_cart_link")

    def get_title(self):
        return self.get_text(self.PAGE_TITLE)

    def add_first_product(self):
        buttons = self.driver.find_elements(*self.ADD_TO_CART_BUTTONS)
        buttons[0].click()

    def add_two_products(self):
        buttons = self.driver.find_elements(*self.ADD_TO_CART_BUTTONS)
        buttons[0].click()
        buttons[1].click()

    def get_cart_count(self):
        return self.get_text(self.CART_BADGE)

    def go_to_cart(self):
        self.click(self.CART_ICON)
