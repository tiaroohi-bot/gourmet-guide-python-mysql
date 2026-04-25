# 🍽️ Gourmet Guide – Food Recommendation System

> A Python + MySQL CLI-based application for exploring food and beverages using search, filtering, and recommendations.

---

## 📌 Overview

Gourmet Guide allows users to discover recipes based on flavor preferences (Sweet, Salty, Spicy, Sour) with powerful features like search, filtering, and full CRUD operations.

---

## 🚀 Features

* 🔎 Search recipes by name
* 🍽️ Filter by food or beverage
* 🌶️ Flavor-based categorization
* 🎯 Random recommendation system
* ✏️ Add, update, and delete items (CRUD)
* 📋 View all items in database

---

## 🛠️ Tech Stack

* **Python**
* **MySQL**
* **PyMySQL**

---

## 🗄️ Database Design

**Table: MenuItems**

| Field       | Description                  |
| ----------- | ---------------------------- |
| id          | Primary key                  |
| flavor      | Sweet / Salty / Spicy / Sour |
| item_type   | Food / Beverage              |
| name        | Item name                    |
| ingredients | Ingredients list             |
| recipe      | Preparation steps            |
| nutrition   | Nutritional info             |
| fun_fact    | Interesting fact             |

---

## ▶️ How to Run

```bash
pip install pymysql
```

Ensure MySQL is running.

Set your password (recommended using environment variable):

```bash
export DB_PASSWORD=your_mysql_password
```

Run the program:

```bash
python main.py
```

---

## 💡 Learning Outcomes

* Database normalization and design
* Python–MySQL integration
* CRUD operations
* CLI-based application development
* Data filtering and search logic

---

## 👩‍💻 Author

**Tia Ahuja**
