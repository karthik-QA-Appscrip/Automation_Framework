from selenium.webdriver.common.by import By

class LoginLocators:

    CONTINUE_WITH_PASSWORD = (
        By.XPATH,
        "//button[normalize-space()='Continue with password']"
    )

    USERNAME = (By.ID, "email")

    PASSWORD = (By.ID, "password")

    LOGIN_BUTTON = (
        By.XPATH,
        "//button[@type='submit']"
    )

    POPUP = (
        By.XPATH,
        "//section[@aria-label='Notifications alt+T']"
    )

    ERROR_MESSAGE = (
        By.XPATH,
        "//p[@class='text-sm text-destructive']"
    )

    ERROR_POPUP = (
        By.XPATH,
        "//section[@aria-label='Notifications alt+T']//div[contains(@class,'leading-5 tracking-[-0.01em] text-foreground')]"
    )

    INVALID_CREDENTIALS_MESSAGE = (
        By.XPATH,
        "//div[@id='radix-_r_3_']"
    )

    CLOSE_BUTTON = (
        By.XPATH,
        "//button[normalize-space()='Close']"
    )

    INVALID_EMAIL_ERROR_MESSAGE = (
        By.XPATH,
        "//p[@class='text-sm text-destructive']"
    )