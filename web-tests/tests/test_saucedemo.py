import sys
import os
sys.path.insert(0, os.path.dirname(os.path.dirname(__file__)))

import pytest
from pages.login_page import LoginPage
from pages.inventory_page import InventoryPage
from pages.cart_page import CartPage
from pages.checkout_page import CheckoutPage

VALID_USER = "standard_user"
VALID_PASS = "secret_sauce"


def test_login_sucesso(driver):
    login = LoginPage(driver)
    login.open()
    login.login(VALID_USER, VALID_PASS)

    inventory = InventoryPage(driver)
    assert inventory.get_title() == "Products"


def test_login_invalido(driver):
    login = LoginPage(driver)
    login.open()
    login.login("usuario_errado", "senha_errada")

    assert "Epic sadface" in login.get_error_message()


def test_adicionar_produto_ao_carrinho(driver):
    login = LoginPage(driver)
    login.open()
    login.login(VALID_USER, VALID_PASS)

    inventory = InventoryPage(driver)
    inventory.add_first_product()

    assert inventory.get_cart_count() == "1"


def test_fluxo_completo_compra(driver):
    # Login
    login = LoginPage(driver)
    login.open()
    login.login(VALID_USER, VALID_PASS)

    # Adiciona 2 produtos
    inventory = InventoryPage(driver)
    inventory.add_two_products()
    assert inventory.get_cart_count() == "2"

    # Vai para o carrinho
    inventory.go_to_cart()
    cart = CartPage(driver)
    assert cart.get_items_count() == 2

    # Checkout
    cart.proceed_to_checkout()
    checkout = CheckoutPage(driver)
    checkout.fill_info("João", "Silva", "12345")
    checkout.continue_checkout()
    checkout.finish_order()

    # Confirmação
    assert checkout.get_confirmation_text() == "Thank you for your order!"
