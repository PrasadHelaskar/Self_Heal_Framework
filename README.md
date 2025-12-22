# Self-Heal Framework (Selenium + Python)

## Overview

This repository contains a **custom Selenium automation framework with a basic self‑healing mechanism**, built using **Python + Pytest**.

The main goal of this project is to explore how modern automation tools handle locator failures and to implement a **lightweight, transparent self‑healing approach** without relying on commercial tools.

This is **not a wrapper around Selenium** and **not a toy project**. It focuses on:

* Practical locator recovery
* Maintainable structure
* Clear separation of responsibilities

---

## Why Self‑Healing?

In real projects, UI tests fail frequently due to:

* Minor DOM changes
* Updated attributes (id, name, xpath)
* UI refactoring without functional changes

Instead of immediately failing the test, this framework:

1. Tries the **primary locator**
2. Falls back to **alternative locators**
3. Updates the locator source automatically (if enabled)

This reduces flaky failures and improves test stability.

---

## Key Features

* JSON‑based locator management (primary + fallback)
* Centralized self‑healing engine
* Automatic fallback resolution
* Custom logging (no print statements)
* Pytest‑based execution
* Page‑Object‑Model friendly structure

---

## Project Structure

```
Self_Heal_Framework/
│
├── core/
│   ├── self_healing_engine.py   # Core healing logic
│   ├── smart_locator.py         # Locator resolution & fallback handling
│
├── utils/
│   ├── json_operations.py       # JSON read/write utilities
│   ├── logger.py                # Custom logging configuration
│
├── locators/
│   └── login_page.json          # Primary + fallback locators
│
├── tests/
│   └── test_login.py            # Sample test cases
│
├── conftest.py                  # Pytest setup
├── requirements.txt
└── README.md
```

---

## Locator Strategy (JSON Driven)

Each element is defined with:

* One **primary locator**
* One or more **fallback locators**

Example:

```json
{
  "username": {
    "primary": {"type": "id", "value": "user-name"},
    "fallback": [
      {"type": "xpath", "value": "//input[@name='user-name']"},
      {"type": "css", "value": "input[data-test='username']"}
    ]
  }
}
```

The framework always prefers the primary locator and switches to fallback only on failure.

---

## How Self‑Healing Works (High Level)

1. Test requests an element by **logical name** (not Selenium locator)
2. Smart Locator fetches primary + fallback locators from JSON
3. Self‑Healing Engine tries each locator in order
4. On success:

   * Element is returned
   * (Optional) locator source is updated
5. On failure:

   * Clear error with logging context

This keeps test scripts clean and readable.

---

## How to Run

### Prerequisites

* Python 3.9+
* Chrome browser
* ChromeDriver (compatible version)

### Setup
---

```bash
pip install -r requirements.txt
```

### Execute Tests

```bash
pytest -v
```

---

## Logging

* Uses Python logging module
* Logs locator attempts and healing decisions
* Designed to integrate with reporting tools (Allure planned)

---

## Current Status

* Core self‑healing logic implemented
* JSON‑based locator strategy complete
* Sample test cases added
* Reporting integration planned

---

## Disclaimer

This project is built as a **learning‑focused engineering exercise**, inspired by tools like Testim, Mabl, and Healenium.

The intention is to **understand the mechanics behind self‑healing**, not to replace enterprise‑grade tools.

---

## Author

**Prasad Helaskar** </br>
Automation Engineer | Python | Selenium | Pytest

---

## Future Enhancements

* Locator reliability scoring
* Healing confidence threshold
* Allure reporting integration
* Parallel execution support

## Note
This framework is actively evolving. Test coverage and locator strategies are being expanded incrementally to reflect real-world automation practices.
