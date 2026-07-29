# Selenium Automation Framework

## Overview

A scalable, maintainable, and reusable Selenium Automation Framework built using **Python**, **Selenium WebDriver**, and **Pytest** following the **Page Object Model (POM)** design pattern.

The framework is designed for enterprise-level web automation and supports cross-browser execution, parallel execution, configurable environments, reporting, logging, screenshot capture, Jenkins CI/CD integration, and reusable utility components.

---

# Tech Stack

- Python
- Selenium WebDriver
- Pytest
- Allure Report
- Pytest HTML Report
- WebDriverManager
- Faker
- OpenPyXL
- Jenkins
- Git & GitHub

---

# Framework Features

- Page Object Model (POM)
- Driver Factory Pattern
- Thread Local Driver Manager
- Base Page Architecture
- Base Test Class
- Explicit Wait Utility
- Assertion Helper
- Config Reader
- JSON Test Data
- Excel Test Data
- Faker Test Data Generation
- Cross Browser Execution
- Headless Execution
- Screenshot Capture on Failure
- Logging
- Automatic Retry of Failed Tests
- Allure Reporting
- Pytest HTML Reporting
- Jenkins CI/CD Pipeline
- GitHub Integration

---

# Project Structure

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

# Framework Components

## Pages

Contains Page Object classes that encapsulate page actions.

## Locators

Stores all page locators separately from test logic.

## Utilities

Contains reusable framework components:

- DriverFactory
- DriverManager (Thread Local)
- BasePage
- BaseTest
- WaitHelper
- AssertionHelper
- ConfigReader
- Logger
- Screenshot Utility
- TestDataManager

## Fixtures

Contains browser initialization and teardown fixtures.

## Test Data

Supports

- JSON
- Excel
- Faker Generated Data

---

# Browser Support

- Google Chrome
- Microsoft Edge
- Mozilla Firefox

---

# Prerequisites

- Python 3.x
- Chrome / Edge / Firefox
- Git
- Allure Command Line

---

# Installation

Clone the repository

```bash
git clone <repository_url>
```

Navigate to the project

```bash
cd Automation_Framework
```

Install dependencies

```bash
pip install -r requirements.txt
```

---

# Test Execution

Run all tests

```bash
pytest
```

Run Smoke Tests

```bash
pytest -m smoke
```

Run in Headless Mode

```bash
pytest --headless
```

Run on Chrome

```bash
pytest --browser chrome
```

Run on Edge

```bash
pytest --browser edge
```

Run on Firefox

```bash
pytest --browser firefox
```

Run Tests in Parallel

```bash
pytest -n 4
```

---

# Reporting

Generate Allure Results

```bash
pytest --alluredir=allure-results
```

Open Allure Report

```bash
allure serve allure-results
```

Generate HTML Report

```bash
pytest --html=reports/report.html
```

---

# Logging

Execution logs are automatically generated inside

```
logs/
```

Each execution creates a timestamped log file.

---

# Screenshots

On test failure, screenshots are automatically

- Captured
- Saved inside `screenshots/`
- Attached to the Allure Report

---

# Configuration

Framework configuration is maintained inside the `config/` directory.

Configurable properties include:

- Application URL
- Browser
- Timeout
- Environment

Supported environments:

- Development
- QA
- UAT

---

# CI/CD

The framework supports automated execution using **Jenkins Pipeline**.

Pipeline includes:

- Source Code Checkout
- Dependency Installation
- Test Execution
- Allure Report Generation
- HTML Report Generation

---

# Design Pattern

This framework follows:

- Page Object Model (POM)
- Factory Design Pattern
- Thread Local Driver Management

---

# Author

**Karthik S**

Automation Test Engineer