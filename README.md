# Selenium Automation Framework

## Overview

This automation framework is developed using Python, Selenium WebDriver, and Pytest. It follows the Page Object Model (POM) design pattern to provide a scalable, reusable, and maintainable test automation solution.

The framework supports cross-browser execution, headless mode, data-driven testing, reporting, logging, and automatic retry of failed test cases.

---

## Features

- Selenium WebDriver
- Pytest
- Page Object Model (POM)
- Driver Factory
- Base Page Architecture
- Base Test Class
- Cross Browser Execution
- Headless Execution
- WebDriverManager
- Allure Reporting
- Pytest HTML Reporting
- Screenshot Capture on Failure
- Automatic Retry
- JSON Test Data
- Excel Test Data
- Logging
- Configurable Environment

---

## Project Structure

```text
Automation_Framework/
│
├── config/
├── constants/
├── fixtures/
├── locators/
├── logs/
├── pages/
├── reports/
├── screenshots/
├── testdata/
├── tests/
├── utilities/
│
├── conftest.py
├── pytest.ini
├── requirements.txt
└── README.md
```

---

## Prerequisites

- Python 3.x
- Google Chrome / Microsoft Edge / Mozilla Firefox
- Allure Command Line
- Git

---

## Installation

Clone the repository:

```bash
git clone <repository_url>
```

Install dependencies:

```bash
pip install -r requirements.txt
```

---

## Test Execution

Run all tests:

```bash
pytest
```

Run in headless mode:

```bash
pytest --headless
```

Run on Chrome:

```bash
pytest --browser chrome
```

Run on Edge:

```bash
pytest --browser edge
```

Run on Firefox:

```bash
pytest --browser firefox
```

---

## Reporting

Generate Allure results:

```bash
pytest --alluredir=allure-results
```

Open Allure Report:

```bash
allure serve allure-results
```

---

## Framework Components

### Pages
Contains Page Object classes.

### Locators
Contains all page locators.

### Utilities
Contains reusable framework utilities such as:

- DriverFactory
- ConfigReader
- Logger
- Screenshot
- WaitHelper
- AssertionHelper
- TestDataManager

### Fixtures

Contains browser and reporting fixtures.

### Test Data

Supports both JSON and Excel based test data.

---

## Logging

Execution logs are generated automatically under the `logs/` directory.

---

## Screenshots

Failure screenshots are automatically captured and attached to the Allure report.

---

## Browser Support

- Chrome
- Edge
- Firefox

---

## Configuration

Framework configuration is managed through the configuration files located in the `config/` directory.

Supported environments:

- Development
- QA
- UAT