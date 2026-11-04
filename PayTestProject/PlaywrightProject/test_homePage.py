#first test with Playwright

from playwright.sync_api import Page, expect
import re
import pytest

LOCAL_URL="file:///C:/Users/User/Downloads/playwright-selectors.html"
#Playwright test no.1: 
# def test_homepage_heading(page: Page):
#     page.goto("https://playwright.dev/")
#     heading= page.get_by_role("heading", level=1, name="playwright")
#     heading.highlight()
#     page.pause()
#     expect(heading).to_be_visible()



#Playwright test no.2:
# @pytest.mark.navi
# def test_get_started_navigation(page: Page):
#     page.goto("https://playwright.dev/")
#     page.pause()
#     link= page.get_by_role("link", name="Get started")
#     link.click()
#     link.highlight()
    
#     expect(
#         page.get_by_role("heading", name="Installation")
#     ).to_be_visible()



#Playwright test no.3: 
#test on playwright-selectors.html
# 
# TODO: Find the button using its role and name.
# TODO: Click it and verify the confirmation text.
@pytest.mark.play1
def test_playwright_selectors_exe(page:Page):
    page.goto(LOCAL_URL)
    page.pause()
    button= page.get_by_role("button", name="Open Details")
    button.click()
    button.highlight()

    expect(
        page.locator("#button-result")).to_have_text(
        "Button clicked! This text appeared after the click.",
        ignore_case=True,
    )

# TODO: Find the email input using its placeholder.
    email_field= page.get_by_placeholder("name@example.com")
    email_field.highlight() 
    expect(email_field).to_be_visible()
    
    email_field.fill("yael@example.com")
    expect(email_field).to_have_value("yael@example.com")

# TODO: Fill in the password field.
    password_field= page.locator("#password-field")
    password_field.highlight() 
    password_field.scroll_into_view_if_needed()
    expect(password_field).to_be_visible()
    password_field.fill("yael1234")
    expect(password_field).to_have_value("yael1234")

# TODO: Select United Kingdom from the dropdown.
    drop_down = page.locator("#country")
    drop_down.highlight()
    drop_down.select_option("United Kingdom")
    expect(drop_down).to_be_visible()

# TODO: Select Premium.
    basic = page.get_by_role("radio", name="Basic")
    premium = page.get_by_role("radio", name="Premium")
    # basic.check()
    # expect(basic).to_be_checked()
    # expect(premium).not_to_be_checked()
    premium.check()
    expect(premium).to_be_checked()
    expect(basic).not_to_be_checked()

# TODO: Check the terms checkbox.
    agreeCeckBox=page.get_by_role("checkbox", name="I agree to the terms") 
    agreeCeckBox.check()
    expect(agreeCeckBox).to_be_checked()

# TODO: Submit the form and verify the confirmation.

# TODO: Click the Details link and verify that a new tab opens.
# TODO: Verify the headline and paragraph on the new page.