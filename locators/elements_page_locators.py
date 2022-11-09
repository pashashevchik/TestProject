from selenium.webdriver.common.by import By


class TextBoxPageLocators:

    # Form field

    FULL_NAME_FIELD_SELECTOR = (By.CSS_SELECTOR, "input[id='userName']")
    EMAIL_FIELD_SELECTOR = (By.CSS_SELECTOR, "input[id='userEmail']")
    CURRENT_ADDRESS_FIELD_SELECTOR = (By.CSS_SELECTOR, "textarea[id='currentAddress']")
    PERMANENT_ADDRESS_FIELD_SELECTOR = (By.CSS_SELECTOR, "textarea[id='permanentAddress']")
    SUBMIT_BUTTON_SELECTOR = (By.CSS_SELECTOR, "button[id='submit']")

    # Created form

    CREATED_FULL_NAME_SELECTOR = (By.CSS_SELECTOR, "#output #name")
    CREATED_EMAIL_SELECTOR = (By.CSS_SELECTOR, "#output #email")
    CREATED_CURRENT_ADDRESS_SELECTOR = (By.CSS_SELECTOR, "#output #currentAddress")
    CREATED_PERMANENT_ADDRESS_SELECTOR = (By.CSS_SELECTOR, "#output #permanentAddress")

