from playwright.sync_api import sync_playwright, expect
import os

def verify_card_skeleton(page):
    """
    This script verifies the card skeleton functionality:
    1. Navigates to the local index.html file.
    2. Takes a screenshot of the initial main category view.
    3. Clicks the first category card.
    4. Takes a screenshot of the resulting sub-card view.
    5. Clicks the 'back' button.
    6. Takes a final screenshot to confirm it returned to the main view.
    """
    # Get the absolute path to the index.html file
    # This is necessary for Playwright to find the file correctly.
    file_path = os.path.abspath('index.html')

    # 1. Arrange: Go to the local HTML file.
    page.goto(f'file://{file_path}')

    # Assert that the main container is visible and the sub-container is hidden.
    expect(page.locator('#main-card-container')).to_be_visible()
    expect(page.locator('#sub-card-container')).to_be_hidden()
    expect(page.locator('#back-button')).to_be_hidden()

    # Take a screenshot of the initial main category view.
    page.screenshot(path='jules-scratch/verification/01_main_view.png')

    # 2. Act: Click the first category card.
    first_card = page.locator('.card').first
    first_card.click()

    # 3. Assert: Check that the sub-cards are now visible and the main cards are hidden.
    expect(page.locator('#main-card-container')).to_be_hidden()
    expect(page.locator('#sub-card-container')).to_be_visible()
    expect(page.locator('#back-button')).to_be_visible()
    # Check that 20 sub-cards were created
    expect(page.locator('#sub-card-container .card')).to_have_count(20)


    # Take a screenshot of the sub-card view.
    page.screenshot(path='jules-scratch/verification/02_sub_view.png')

    # 4. Act: Click the 'back' button.
    back_button = page.locator('#back-button')
    back_button.click()

    # 5. Assert: Check that the view has returned to the main category screen.
    expect(page.locator('#main-card-container')).to_be_visible()
    expect(page.locator('#sub-card-container')).to_be_hidden()
    expect(page.locator('#back-button')).to_be_hidden()
    # Check that 8 main cards are present
    expect(page.locator('#main-card-container .card')).to_have_count(8)

    # Take a final screenshot to confirm the return to the main view.
    page.screenshot(path='jules-scratch/verification/03_return_to_main_view.png')


# Boilerplate to run the verification
with sync_playwright() as playwright:
    browser = playwright.chromium.launch(headless=True)
    page = browser.new_page()
    verify_card_skeleton(page)
    browser.close()