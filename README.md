# OrangeHRM Test Automation (Python + Pytest)

This project is an automated testing suite for the **OrangeHRM** Open Source application. It was developed as part of **Assignment 5** for the Software Quality Assurance and Testing course. 

## 🎯 Project Overview
The suite covers critical Smoke testing scenarios using **Python**, **Selenium WebDriver**, and the **Pytest** framework. It implements a complete test lifecycle, detailed logging, and automated HTML reporting with screenshots.

---

## 🛠 Tech Stack
* **Language:** Python 3.10+
* **Framework:** [Pytest](https://docs.pytest.org/)
* **Tool:** [Selenium WebDriver](https://www.selenium.dev/)
* **Reporting:** `pytest-html`
* **Logging:** Python `logging` module

---

## ✨ Features Implemented (Assignment Requirements)
- **Lifecycle Management (30 pts):** Clear separation of `Setup` and `Teardown` using Pytest fixtures in `conftest.py`.
- **Logging Framework (30 pts):** All test steps, start/end markers, and errors are logged into `logs/automation.log`.
- **HTML Report (40 pts):** Detailed execution summary with `pass/fail` status.
- **Automatic Screenshots:** The system captures a screenshot after every test (including failures) and embeds it directly into the HTML report.
- **Explicit Waits:** Uses `WebDriverWait` for stable element interaction on dynamic SPA pages.

---

## 📂 Project Structure
```text
sqat_5/
├── tests/                # Test case files
│   ├── test_login.py     # Login functionality tests
│   ├── test_admin.py     # Admin user search tests
│   └── test_pim.py       # PIM module navigation tests
├── conftest.py           # Project configuration (Setup/Teardown, Screenshots)
├── logs/                 # Folder for execution log files
├── reports/              # Folder for HTML reports and screenshots
└── requirements.txt      # Project dependencies


⚙️ Installation & Setup
Clone the repository:

Bash

git clone <>
cd sqat_5
Install dependencies:

Bash
pip install -r requirements.txt
(Or manually: pip install selenium pytest pytest-html)

🏃 How to Run the Tests
To execute all tests and generate the self-contained HTML report, run:

Bash
py -m pytest --html=reports/report.html --self-contained-html
After execution, open reports/report.html in your browser to see the results and screenshots.
