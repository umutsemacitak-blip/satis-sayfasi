from playwright.sync_api import sync_playwright, expect
import os

def verify_styling(page):
    """
    This script verifies the new dark theme and glassmorphism styling:
    1. Navigates to the local index.html file.
    2. Takes a screenshot to verify the dark theme and card styles.
    3. Hovers over the first card.
    4. Takes another screenshot to verify the hover glow effect.
    """
    # Get the absolute path to the index.html file
    file_path = os.path.abspath('index.html')

    # 1. Arrange: Go to the local HTML file.
    page.goto(f'file://{file_path}')

    # Wait for the cards to be rendered
    page.wait_for_selector('.card')

    # Take a screenshot of the initial view.
    page.screenshot(path='jules-scratch/verification/01_dark_theme_view.png')

    # 2. Act: Hover over the first card.
    first_card = page.locator('.card').first
    first_card.hover()

    # Wait for the transition to complete
    page.wait_for_timeout(300)

    # Take a screenshot of the hover effect.
    page.screenshot(path='jules-scratch/verification/02_hover_effect_view.png')


# Boilerplate to run the verification
with sync_playwright() as playwright:
    browser = playwright.chromium.launch(headless=True)
    page = browser.new_page()
    verify_styling(page)
    browser.close()