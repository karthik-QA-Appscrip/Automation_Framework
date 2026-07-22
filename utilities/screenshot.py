import os
from datetime import datetime


class Screenshot:

    @staticmethod
    def capture(driver, test_name):

        folder = "screenshots"
        os.makedirs(folder, exist_ok=True)

        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        file_name = f"{test_name}_{timestamp}.png"

        path = os.path.join(folder, file_name)

        success = driver.save_screenshot(path)

        print(f"Screenshot Success: {success}")
        print(f"Screenshot Path: {os.path.abspath(path)}")

        return path