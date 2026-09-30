from playwright.sync_api import Page, expect

def test_saucedemo_homepage(page: Page):
    page.goto("https://www.saucedemo.com/")
    username_input = page.get_by_placeholder("Username")
    expect(username_input).to_be_visible()
    username_input.fill("standard_user")
    password_input = page.get_by_placeholder("Password")
    password_input.fill("secret_sauce")
    login_button = page.get_by_role("button", name="Login")
    login_button.click()
    products_title = page.get_by_text("Products")
    expect(products_title).to_be_visible()
