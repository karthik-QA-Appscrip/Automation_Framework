from utilities.configReader import ConfigReader
from utilities.jsonReader import JsonReader


class TestData:

    config = ConfigReader()

    login_data = JsonReader.read_json(
        config.get_json_path()
    )

    valid_username = login_data["credentials"]["valid"]["username"]
    valid_password = login_data["credentials"]["valid"]["password"]

    invalid_username = login_data["credentials"]["invalid"]["username"]
    invalid_password = login_data["credentials"]["invalid"]["password"]

    invalid_email_cases = login_data["invalidEmails"]

    contact_first_name = login_data["contact"]["first_name"]
    contact_email = login_data["contact"]["email"]