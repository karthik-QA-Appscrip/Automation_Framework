from threading import local

class DriverManager:

    _driver = local()

    @classmethod
    def set_driver(cls, driver):
        cls._driver.instance = driver

    @classmethod
    def get_driver(cls):
        return cls._driver.instance

    @classmethod
    def quit_driver(cls):
        if hasattr(cls._driver, "instance"):
            cls._driver.instance.quit()
            del cls._driver.instance