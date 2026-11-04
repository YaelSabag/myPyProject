######## Yael Sabag --------- ID:209438985 ########

import re
from playwright.sync_api import Page, expect
import pytest
import consts

GITHUB_FORM_URL = "https://github.com/yashago/hadasim-qa-pytest/blob/main/tests/playwright/src/playwright_registration_form.html"
FILE_PATH = f"https://htmlpreview.github.io/?{GITHUB_FORM_URL}"




################################    Main test    ###############################
def test_registration_form(page: Page):
    # Open the registration form
    page.goto(FILE_PATH)
    printAccessibilityTree(page)
    page.pause()
    fillInFullForm(page)
    validateResetForm(page)
    fillInFullForm(page)
    validateSubmitForm(page)


################   HEADER test: Registration / Preferences / Google Map / Help / Native dialog / Playwright Docs   ################
def test_header(page: Page):
    page.goto(FILE_PATH)

    validateRegistrationLink(page)
    validatePreferencesLink(page)
    googleMapsLInk(page)
    validateHelpLink(page)
    ConfirmNativeDialogLink(page)
    validatePlaywrightDocsLink(page)
    page.pause()


#######################   Fill in the full form (calls a function for each field)   ######################
def fillInFullForm(page):
    data = consts.REGISTRATION_FORM
    fillInFirstName(page, data["firstName"])
    fillInlastName(page, data["lastName"])
    fillInEmail(page, data["email"])
    fillInEmailConfirmation(page, data["email"])
    fillInPassword(page, data["password"])
    fillInPhoneNumber(page, data["phone"])
    fillInDateOfBirth(page, data["dateOfBirth"])
    selectCountry(page, data["country"])
    fillInCity(page, data["city"])
    fillPersonalWeb(page, data["personalWebsite"])
    selectGender(page, data["gender"])
    selectOccupation(page, data["occupation"])
    fillShortIntro(page, data["shortIntro"])
    selectExperience(page, data["experience"])
    selectFavBrowser(page, data["favoriteBrowser"])
    selectTopicsInterest(page, data["topicsInterest"])
    selectPreferredContact(page, data["preferredContact"])
    checkTerms(page, data["termsLabel"])

    page.pause()



#-------------------------------------------   Form field functions   ---------------------------------------------
def fillInFirstName(page, firstName):
    #By role, preferred method
    page.get_by_role("textbox", name="First name").fill(firstName)
    print(f"\nThe first name: {firstName}")
    # #By label, preferred method
    # page.get_by_label("First name").fill("Doe")

    # #By placeholder, good option if the placeholder is unique and descriptive
    # page.get_by_placeholder("e.g. Alex").fill("John")

    # #By locator, good option if the locator is unique and descriptive
    # page.locator("#firstName").fill("Doe")

    # #By locator, Usually unnecessary
    # page.locator('input[id="firstName"]').fill("John")
    # page.fill('input[name="firstName"]', "Doe")

def fillInlastName(page, lastName):
    page.get_by_role("textbox", name="Last name").fill(lastName)
    print(f"\nThe last name: {lastName}")

def fillInEmail(page, Gmail):
    page.get_by_placeholder("alex@example.com").fill(Gmail)
    print(f"\nThe Gmail: {Gmail}")


def fillInEmailConfirmation(page, confirmGmail):
    page.get_by_role("textbox", name="Confirm email address").fill(confirmGmail)
    print(f"\nThe confirm Gmail: {confirmGmail}")


def fillInPassword(page, password):
    page.get_by_role("textbox", name="Password").fill(password)
    print(f"\nThe password: {password}")


def fillInPhoneNumber(page, phone):
    page.get_by_role("textbox", name="Phone number").fill(phone)
    print(f"\nThe phone: {phone}")


def fillInDateOfBirth(page, dateOfBirth):
    #By label, preferred method
    datePicker = page.get_by_label("Date of birth")
    datePicker.fill(dateOfBirth)
    datePicker.scroll_into_view_if_needed()
    datePicker.highlight()
    print(f"\nThe dateOfBirth: {dateOfBirth}")


def selectCountry(page,countryValue):
    countrySelect=page.get_by_role("combobox", name="Country")
    countrySelect.select_option(countryValue)
    countrySelect.scroll_into_view_if_needed()
    print(f"\nThe country: {countryValue}")

def fillInCity(page, city):
    cityVal=page.get_by_role("textbox", name="City")
    cityVal.fill(city)
    cityVal.scroll_into_view_if_needed()
    print(f"\nThe city: {city}")

def fillPersonalWeb(page, personalWeb):
    personalVal=page.get_by_role("textbox", name="Personal website")
    personalVal.fill(personalWeb)
    personalVal.scroll_into_view_if_needed()
    print(f"\nThe personal web: {personalWeb}")


def selectGender(page, gender):
    page.get_by_role("radio", name=gender).check()
    print(f"\nThe gender web: {gender}")

def selectOccupation(page,OccupationValue):
    OccupationSelect=page.get_by_role("combobox", name="Occupation")
    OccupationSelect.select_option(OccupationValue)
    print(f"\nThe Occupation: {OccupationValue}")

def fillShortIntro(page, shortIntro):
    page.get_by_role("textbox", name="Short introduction").fill(shortIntro)
    print(f"\nThe shortIntro: {shortIntro}")

def selectExperience(page,ExperienceValue):
    ExperienceSelect=page.get_by_role("combobox", name="Years of experience")
    ExperienceSelect.select_option(ExperienceValue)
    ExperienceSelect.scroll_into_view_if_needed()
    print(f"\nThe Experience: {ExperienceValue}")

def selectFavBrowser(page,FavBrowserValue):
    FavBrowsereSelect=page.get_by_role("combobox", name="Favorite browser")
    FavBrowsereSelect.select_option(FavBrowserValue)
    FavBrowsereSelect.scroll_into_view_if_needed()
    print(f"\nThe Favorite Browser: {FavBrowserValue}")

def selectTopicsInterest(page, topicsInterestValue):
    page.get_by_role("checkbox", name=topicsInterestValue).check()
    print(f"\nThe topics interest: {topicsInterestValue}")

def selectPreferredContact (page, PreferredContact):
    page.get_by_role("radio", name=PreferredContact).check()
    print(f"\nThe preferred contact: {PreferredContact}")

def checkTerms(page, checkTerms):
    page.get_by_role("checkbox", name=checkTerms).check()
    print(f"\n check Terms: {checkTerms}")


#----------------------------------------------------------------------------------------------------------------------



##########################################   Reset button test   ##########################################
def validateResetForm(page:Page):
    print("\nClicking Reset and checking the message")
    resetButton = page.get_by_role("button", name="Reset form")
    resetButton.click()

    # Save a snapshot of the message right after the click (it disappears after 3 seconds)
    statusSnapshot = page.get_by_role("status").aria_snapshot()
    print("statusSnapshot",statusSnapshot)
    assert consts.REGISTRATION_FORM["resetConfirmationText"] in statusSnapshot


##########################################   Submit button test   ##########################################
def validateSubmitForm(page: Page):
    print("\nClicking Submit and checking the success dialog")
    submitButton = page.get_by_role("button", name="Submit registration")
    submitButton.scroll_into_view_if_needed()
    submitButton.highlight()
    print("\nClicking on the submit button")
    submitButton.click()

    # Check that the dialog is open (its name is the heading text)
    dialog = page.get_by_role("dialog", name=consts.REGISTRATION_FORM["submitHeaderText"])
    expect(dialog).to_be_visible()

    # Check the heading
    expect(dialog.get_by_role("heading", level=2, name=consts.REGISTRATION_FORM["submitHeaderText"])).to_be_visible()

    # Check the message shows the name and email from the form
    firstName = consts.REGISTRATION_FORM["firstName"]
    email = consts.REGISTRATION_FORM["email"]
    expectedMessage = f"Thank you, {firstName}! Your demo registration for {email} has been received."
    expect(dialog).to_contain_text(expectedMessage)

    # Close the dialog
    closeButton = dialog.get_by_role("button", name="Close")
    expect(closeButton).to_be_enabled()
    closeButton.click()
    expect(dialog).to_be_hidden()


###  HEADER ###
##########################################   Registration link test   ########################################
def validateRegistrationLink(page:Page):
    print("\nClicking Registration link")
    page.pause()
    registrationLink = page.get_by_role("link", name="Registration")
    registrationLink.highlight()
    registrationLink.click()
    # Check that the URL ends with #registration
    expect(page).to_have_url(re.compile(r"#registration$"))




###  HEADER ###
##########################################   Preferences link test   #########################################
def validatePreferencesLink(page:Page):
    print("\nClicking Preferences link")
    page.pause()
    preferencesLink = page.get_by_role("link", name="Preferences")
    preferencesLink.highlight()
    preferencesLink.click()
    # Check that the URL ends with #preferences
    expect(page).to_have_url(re.compile(r"#preferences$"))



###  HEADER ###
##########################################   Playwright Docs link test   ##########################################

def validatePlaywrightDocsLink(page: Page):
    print("\nClicking Playwright Docs link")
    page.pause()
    # 1. Find the link
    playLink = page.get_by_role("link", name="Playwright documentation")
    playLink.scroll_into_view_if_needed()
    playLink.highlight()

    # 2. The link opens a new tab, so wait for it while clicking
    with page.expect_popup() as popup_info:
        playLink.click()

    # 3. Save the new tab and wait for it to load
    newTab = popup_info.value
    newTab.wait_for_load_state()

    # 4. Check the new tab (not page)
    expect(newTab).to_have_url(re.compile(r"^https://playwright\.dev/?"))
    heading = newTab.get_by_role("heading", level=1, name="Playwright")
    heading.highlight()
    expect(heading).to_be_visible()
    print("\n validate Playwright Docs Link")

    # 5. Close the new tab (page is still on the form)
    newTab.close()
    # page.bring_to_front()


###  HEADER ###
##########################################   Help link test   ################################################
def validateHelpLink(page:Page):
    print("\nClicking Help link and checking the dialog")
    helpLink = page.get_by_role("link", name="Help")
    # page.pause()
    helpLink.scroll_into_view_if_needed()
    helpLink.highlight()
    helpLink.click()

    dialog = page.get_by_role("dialog", name="Help")
    expect(dialog).to_be_visible()

    printAccessibilityTree(page)
    dialog = page.get_by_role("dialog", name=consts.REGISTRATION_FORM["modalHeaderText"])
    expect(dialog).to_be_visible()
    expect(dialog.get_by_role("heading", level=2, name=consts.REGISTRATION_FORM.get("modalHeaderText"))).to_be_visible()

    dialogOkButton = dialog.get_by_role("button", name=consts.REGISTRATION_FORM.get("modalButtonText"))
    expect(dialogOkButton).to_be_visible()
    expect(dialogOkButton).to_be_enabled()
    dialogOkButton.click()


###  HEADER ###
##########################################   Native confirm dialog test   ##########################################
def ConfirmNativeDialogLink(page: Page):
    print("\nClicking Native confirm dialog link")
    # Accept the dialog
    page.once("dialog", lambda dialog: dialog.accept())
    page.get_by_role("link",name="Native confirm dialog").click()
    print("\nclick accpet ")

    # Dismiss the dialog
    page.once("dialog", lambda dialog: dialog.dismiss())
    page.get_by_role("link",name="Native confirm dialog").click()
    print("\nclick dismiss")


###  HEADER ###
##########################################   Google Map link test   ##########################################
def googleMapsLInk(page:Page):
    print("\nClicking Google Map link")
    page.pause()
    mapLink = page.get_by_role("link", name="Google Map")
    mapLink.highlight()
    mapLink.click()
    expect(page).to_have_url(re.compile(r"#map$"))

    mapIframe = page.locator("iframe[title=\"Google Map showing Tel Aviv, Israel\"]")

    expect(mapIframe).to_have_attribute(
        "src", re.compile(r"q=Tel\+Aviv,\+Israel")
    )
    mapIframe.scroll_into_view_if_needed()

    navButton = mapIframe.content_frame.get_by_role( "link", name="Open in Maps (opens in new tab)")

    expect(navButton).to_be_visible()
    expect(navButton).to_be_enabled()
    expect(navButton).to_have_attribute(
        "href", re.compile(r"^https://maps\.google\.com/")
    )

    # The map opens in a new tab
    with page.expect_popup() as newWindowsContext:
        navButton.click()

    newPage = newWindowsContext.value
    expect(newPage).to_have_url(re.compile("https://www.google.com/maps/.*") )
    newPage.close()



##########################################   Print the accessibility tree (also returns it)   ##########################################
def printAccessibilityTree(page):
    pageAccesibility = page.locator("body").aria_snapshot()
    print(f"pageAccesibility: {pageAccesibility}")
    return pageAccesibility