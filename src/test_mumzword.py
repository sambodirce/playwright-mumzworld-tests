import time
from playwright.sync_api import sync_playwright


def test_mumzword():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        page = browser.new_page()

        page.goto("https://www.mumzworld.com/en")
        time.sleep(5)
        try:
            # Wait for the close button and check visibility
            close_button_locator = page.locator('xpath=//*[@id="close"]')
            if close_button_locator.is_visible():
                close_button_locator.click()
            else:
                print("Promo pop-up element is not visible")

            # Get the actual page title
            actual_title = page.title()

            # Define the expected title
            expected_title = "#1 Mother, Child & Baby Shop in the UAE - Mumzworld"

            # Assert that the page title matches the expected title
            assert actual_title == expected_title, f"Expected '{expected_title}', but got '{actual_title}'"

            # Locate search bar and perform search
            search_bar = page.locator('#search_textbox')
            search_bar.fill('book')
            search_bar.press('Enter')

            # Wait for search results to load and add item to cart
            page.locator("li").filter(has_text="46LeapFrog - Learning Friends").locator("#add_cart_button").click()

            # Click on the cart
            cart_link = page.get_by_role("link", name="Cart")
            cart_link.click()
            time.sleep(5)
            # Increase the quantity of the item
            for i in range(4):
                page.get_by_role("button", name="Increase Quantity").click()
                time.sleep(1)

            # Assert that the quantity increased correctly
            quantity_locator = page.get_by_role("spinbutton")
            quantity_value = int(quantity_locator.input_value())
            assert int(quantity_value) == 5, f"Expected quantity to be 5, but got {quantity_value}"

            # Proceed to checkout
            page.get_by_role("button", name="Proceed to Checkout").click()
            page.get_by_role("link", name="Create Account").click()

            # Fill out the form
            page.get_by_placeholder("First name").fill("Dirce")
            page.get_by_placeholder("Last name").fill("Sambo")
            page.get_by_placeholder("Email").fill("sambodirce@gmail.com")
            page.get_by_placeholder("Password").fill("Test!123")
            page.get_by_role("button", name="Create Account").click()
            time.sleep(5)


        except Exception as e:
            print(f"Test failed: {e}")

        # Close the browser after the test
        browser.close()
