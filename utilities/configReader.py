import configparser

class ConfigReader:

    def __init__(self) -> None:

        self.config = configparser.ConfigParser()

        self.config.read("config/dev.ini")

    def get_browser(self):
        return self.config["DEFAULT"]["browser"]

    def get_url(self):
        return self.config["DEFAULT"]["url"]

    def get_timeout(self):
        return int(self.config["DEFAULT"]["timeout"])

    def get_excel_path(self):
        return self.config["DEFAULT"]["excel_path"]

    def get_sheet_name(self):
        return self.config["DEFAULT"]["sheet_name"]

    def get_json_path(self):
        return self.config["DEFAULT"]["json_path"]

    def get_retry_count(self):
        return int(self.config["DEFAULT"]["retry_count"])

    def get_retry_delay(self):
        return int(self.config["DEFAULT"]["retry_delay"])

    # def get_valid_username(self):
    #     return self.config["DEFAULT"]["valid_username"]

    # def get_valid_password(self):
    #     return self.config["DEFAULT"]["valid_password"]

    # def get_invalid_username(self):
    #     return self.config["DEFAULT"]["invalid_username"]

    # def get_invalid_password(self):
    #     return self.config["DEFAULT"]["invalid_password"]