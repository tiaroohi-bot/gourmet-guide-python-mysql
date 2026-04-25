# 🍽️ Gourmet Guide – Food Recommendation System

## 📌 Overview

Gourmet Guide is an interactive Python and MySQL-based application that allows users to explore food and beverage options based on flavor preferences. It includes features like search, filtering, CRUD operations, and random recommendations.

---

## 🚀 Features

* Flavor-based filtering (Sweet, Salty, Spicy, Sour)
* Search recipes by name
* Filter by food or beverage
* Add, update, and delete items (CRUD operations)
* Random recommendation system
* View all items in database
* Interactive CLI interface

---

## 🛠️ Tech Stack

* Python
* MySQL
* PyMySQL

---

## 🗄️ Database Design

Uses a single optimized table:

**MenuItems**

* id
* flavor
* item_type
* name
* ingredients
* recipe
* nutrition
* fun_fact

---

## ▶️ How to Run

1. Install dependency:

```bash
pip install pymysql
```

2. Ensure MySQL is running

3. Update credentials in code:

```python
DB_PASSWORD = "your_mysql_password"
```

4. Run:

```bash
python main.py
```

---

## 💡 Learning Outcomes

* Database design and normalization
* Python–MySQL integration
* CRUD operations
* CLI-based application development
* Data filtering and search logic

---

## 👩‍💻 Author

Tia Ahuja
