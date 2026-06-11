# Playwright Python Portfolio

This is a small UI test automation project using Python, Pytest, and Playwright.
I made it as a portfolio project to show how I write end-to-end tests for a web
application in a clear and maintainable way.

The target site is [Sauce Demo](https://www.saucedemo.com/), a demo e-commerce
site that is commonly used for automation practice.

## What I Focused On

- Writing tests that are easy to read
- Keeping page interactions in Page Object classes
- Using Pytest fixtures for repeated setup
- Covering both happy paths and validation/error cases
- Keeping the project small enough to understand quickly

## Scenarios Covered

### Login

- Login with a valid user
- Login fails with a wrong username
- Login fails with a wrong password
- Login fails when the username is empty
- Login fails when the password is empty
- Locked-out user cannot log in

### Products

- Sort products by name, A to Z
- Sort products by name, Z to A
- Sort products by price, low to high
- Sort products by price, high to low
- Add a product to the cart
- Remove a product from the cart
- Check the cart badge count

### Cart

- Open the cart page
- Continue shopping from the cart
- Remove products from the cart
- Check that removed products are no longer shown

### Checkout

- Complete checkout from cart to order confirmation
- Go back to the product page after checkout
- Show an error when first name is missing
- Show an error when last name is missing
- Show an error when postal code is missing
- Cancel checkout and return to the cart

## How To Run

Create a virtual environment:

```bash
python -m venv .venv
source .venv/bin/activate
```

Install dependencies:

```bash
pip install -r requirements.txt
playwright install
```

Run the tests:

```bash
pytest
```

Run with the browser visible:

```bash
pytest --headed
```

Run one test file:

```bash
pytest tests/test_checkout.py
```

## Notes

The tests are grouped by feature area in the `tests/` folder. The page classes
are in the `pages/` folder, so the tests can describe user behavior without too
much locator detail.

I used parametrized tests for product sorting because the same idea is checked
in a few different directions. For checkout and login, I included both successful
flows and common failure cases because those are usually important parts of a UI
test suite.
