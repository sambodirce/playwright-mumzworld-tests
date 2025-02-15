# Playwright Tests for Mumzworld

This repository contains automated tests for the **Mumzworld** website using **Playwright** and **pytest**. The tests are designed to verify key functionalities of the Mumzworld webstore, including searching for products, adding items to the cart, adjusting quantities, and user registration.

## Features
The tests include the following actions:
- **Open the Mumzworld webstore**: Navigate to the home page of the Mumzworld website.
- **Search for a product**: Perform a search to find a product by name.
- **Add the product to the shopping bag**: Add the selected product to the cart.
- **Go to the view bag page**: Navigate to the shopping bag (cart) to review the selected items.
- **Increase quantity to 5 items**: Increase the quantity of the added product to 5.
- **Proceed to checkout**: Start the checkout process.
- **Register a new user**: Complete the registration form to create a new user account.

## Prerequisites
- **Python 3.11+**
- **Playwright**: The Playwright package to automate browsers.
- **pytest**: Testing framework for running the tests.
- **GitHub Actions**: For continuous integration and running tests on push/pull requests.

## Setup

### 1. Clone the repository
```bash
git clone https://github.com/sambodirce/playwright-mumzworld-tests.git
cd playwright-mumzworld-tests
