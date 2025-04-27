<p align="center"><img src="static/md_logo.png"></p>

<h1 align="center">Flask Todo App</h1>

<div align="center">
  <img src="https://img.shields.io/badge/OS-Linux%2FWindows-blue" alt="OS" />
  <img src="https://img.shields.io/badge/Made%20with-Python%203.10-blue" alt="Python" />
  <img src="https://img.shields.io/badge/Framework-Flask-orange" alt="Flask" />
  <img src="https://img.shields.io/badge/Database-SQLite3-lightgrey" alt="Database" />
  <img src="https://img.shields.io/badge/License-MIT-green" alt="License" />
  <img src="https://img.shields.io/badge/Maintained-Yes-brightgreen" alt="Maintained" />
  <img src="https://img.shields.io/badge/Status-Under%20Development-yellow" alt="Status" />
  <p><strong>A simple and clean **Todo List** project built with **Flask**, **SQLite**, **SQLAlchemy**, and **Bootstrap**.</strong></p>

</div>

---

## 📂 Project Structure

```bash
  project-root
        │
        ├──data/
        │     └──todo.db
        ├──db_managers/
        │     ├──__init__.py
        │     ├──db_mysql.py
        │     └──db_sqlite.py
        ├──docs/
        │     └──todo-screenshots.png
        ├──logs/
        │     ├──logs.csv
        │     └──logs.json
        ├──my_logging/
        │     ├──__init__.py
        │     ├──log_csv.py
        │     └──log_json.py
        ├──static/
        │     ├──logo.png.png
        │     ├──md_logo.png
        │     └──styles.css
        ├──templates/
        │     └──index.html
        ├──.gitignore
        ├──README.md
        └──requirements.txt
```
---
## 🥷 Features
- Add new Todo items
- Mark Todo items as complete/incomplete
- Delete Todo items
- Event logging (CSV or JSON format)
- Uses SQLite by default (optional MySQL support)
- Clean and responsive UI with Bootstrap 4
- Modular code structure (separated by responsibility)

---

## 🚀 Quick Start

1. Clone or download this repository.
2. Create and activate a virtual environment:
3. Install the required dependencies.
4. Run the app.
5. Open your browser and go to.

```bash
    python -m venv venv
    source venv/bin/activate    # For Linux/Mac
    venv\Scripts\activate       # For Windows
    pip install -r requirements.txt
    python app.py
```
```cpp
    http://127.0.0.1:5000/
```

---

## 🛠️ Database Setup
- By default, the project uses SQLite.
- To switch to MySQL:
1. Update your database credentials inside db_managers/db_mysql.py.
2. In app.py, replace:
```python
from db_managers.db_sqlite import get_db, Todo
```
with:
```python
from db_managers.db_mysql import get_db, Todo
```
3. Install the required MySQL driver:
```bash
    pip install pymysql
```

---

## 📜 Logging Events

- Logs are stored by default in a CSV file (logs/logs.csv).
- If you prefer JSON logs:
- In app.py, change:
```python
from my_logging.log_csv import log
```
to:
```python
from my_logging.log_json import log
```

---

## ✨ Important Notes
- index.html should be placed directly inside the templates/ folder.
- Static files (CSS, images) are loaded using Flask’s url_for('static', filename='...').
- Database file (todo.db) and log files are created automatically if not present.

---

## 🤝 Contributing

Contributions are welcome!
Feel free to submit Pull Requests, Issues, or Suggestions. 🚀

---

## 📃 License

This project is licensed under the MIT License.
You are free to use, modify, and distribute it. ✅

---

### ✨ Made by https://de.masterschool.com/ instructors and structured by Ehsan with pride.