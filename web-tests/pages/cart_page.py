from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from pages.base_page import BasePage


class CartPage(BasePage):
    CART_ITEMS = (By.CLASS_NAME, "cart_item")
    CHECKOUT_BUTTON = (By.ID, "checkout")

    def get_items_count(self):
        # Espera pelo menos 1 item aparecer antes de contar
        self.wait.until(EC.presence_of_element_located(self.CART_ITEMS))
        return len(self.driver.find_elements(*self.CART_ITEMS))

    def proceed_to_checkout(self):
        self.click(self.CHECKOUT_BUTTON)