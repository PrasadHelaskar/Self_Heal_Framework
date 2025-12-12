 ## 🚀 Self-Healing Automation Framework (Python + Selenium + Pytest)

Automatically heal broken Selenium locators using DOM analysis, fuzzy matching, similarity scoring, and smart fallback strategies.
Inspired by tools like Healenium, built completely in Python + Pytest + Selenium.

## 📖 Overview

Selenium UI tests often become flaky when UI changes break locators.
This framework solves that problem by automatically:

Detecting locator failures

Searching DOM for matching elements

Computing similarity score

Updating locator repository

Rerunning the test with healed locator

Logging everything with Allure reporting

This results in stable, maintenance-friendly UI automation, even when your UI changes frequently.

## ✨ Key Features
### 🔹 Smart Locator Engine

JSON-based locator store

Primary + fallback locators

Auto-update healed locators

### 🔹 Self-Healing Mechanism

Fuzzy matching (FuzzyWuzzy)

Levenshtein distance

Attribute similarity scoring

DOM scanning & ranking

### 🔹 Custom Smart WebDriver

Wraps Selenium WebDriver

Automatically retries & heals locators

Enhanced logging

### 🔹 Pytest Integration

Custom plugin: pytest_self_heal.py

Auto-rerun failed tests after healing

Heal status included in test summary

### 🔹 DOM Snapshotting

Saves before and after HTML state

Useful for debugging UI changes

### 🔹 Allure Reporting

Healing steps

Healed locator

Similarity score

DOM snapshot attachments

## 🏗 Architecture
```bash
                ┌───────────────────────────────────────────┐
                │               Test Case (Pytest)           │
                └──────────────────────────┬─────────────────┘
                                           │
                                 calls smart_find()
                                           │
                     ┌─────────────────────▼──────────────────────┐
                     │            Smart WebDriver                 │
                     └─────────────────────┬──────────────────────┘
                                           │
                         tries primary locator → fails?
                                           │ yes
                     ┌─────────────────────▼──────────────────────┐
                     │           Self-Healing Engine              │
                     │  - fallback locators                       │
                     │  - DOM scanning                            │
                     │  - similarity engine                       │
                     └─────────────────────┬──────────────────────┘
                                           │
                                 healed? yes/no
                                           │
                       updates JSON + reruns test after heal

```
## 📁 Folder Structure

self_heal_framework/</br>
│</br>
├── core/</br>
│   ├── smart_driver.py</br>
│   ├── smart_locator.py</br>
│   ├── similarity.py</br>
│   ├── locator_store.py</br>
│   ├── dom_parser.py</br>
│   └── logger.py</br>
│</br>
├── locators/</br>
│   ├── locators.json</br>
│   └── backup_locators.json</br>
│</br>
├── snapshots/</br>
│   ├── before/</br>
│   ├── after/</br>
│   └── diff/</br>
│</br>
├── plugins/</br>
│   └── pytest_self_heal.py </br>
│</br>
├── config/</br>
│   ├── settings.yaml </br>
│   └── environment.json </br>
│ </br>
├── tests/ </br>
│   └── test_login.py </br>
│ </br>
├── reports/ </br>
│   ├── allure-results/ </br>
│   └── healing-log.txt </br>
│ </br>
├── utils/ </br>
│   ├── file_utils.py </br>
│   ├── retry.py </br>
│   └── json_utils.py </br>
│ </br>
├── requirements.txt </br>
├── conftest.py </br>
└── README.md </br>

## ⚙ Installation
### 1️⃣ Clone the repository
```bash  
  git clone https://github.com/<your-username>/self-heal-framework.git </br>
  cd self-heal-framework
```

### 2️⃣ Install dependencies
```bash
  pip install -r requirements.txt
```

### 3️⃣ Install Allure (optional but recommended)

Follow installation:
https://docs.qameta.io/allure/#_installing_a_commandline

## 🔍 How It Works
When a locator fails:

Framework fetches alternative locators from locators.json
Tries fallback locators
If none work → performs DOM scan
Computes similarity score using:
Levenshtein distance
Fuzzy attribute matching
Text similarity
Chooses best candidate
Updates locator store automatically
Reruns the test through Pytest plugin
Logs the entire healing process

## ▶️ Usage
```python
Import SmartDriver
from core.smart_driver import SmartDriver

def test_login():
    driver = SmartDriver()
    driver.open("https://example.com")

    login_btn = driver.find("login_button")
    login_btn.click()

    driver.quit()

Sample locator entry (locators.json)
{
  "login_button": {
    "primary": "//button[@id='login']",
    "fallbacks": [
      "//button[text()='Login']",
      "//button[contains(@class,'btn-primary')]"
    ]
  }
}
```

## ⚙ Configuration (settings.yaml)
healing:
  similarity_threshold: 70 </br>
  enable_snapshot: true </br>
  snapshot_path: snapshots/ </br>

retry:
  max_attempts: 2

## 📊 Reporting (Allure)

Run with Allure:
```bash
pytest --alluredir=reports/allure-results
```

Generate report:
```bash
allure serve reports/allure-results
```

Allure will display:
Broken locator
Healed locator
Healing confidence score
DOM snapshots (before/after)
Plugin rerun status
