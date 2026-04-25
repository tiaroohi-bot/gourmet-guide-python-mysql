import pymysql
import random
import os

# ================== CONFIG ==================
DB_HOST = "localhost"
DB_USER = "root"
DB_PASSWORD = os.getenv("DB_PASS")  # no password stored in code
DB_NAME = "GourmetGuide"

TABLE_NAME = "MenuItems"
FLAVORS = ["Sweet", "Salty", "Spicy", "Sour"]

# ================== CONNECTION ==================
def get_connection(database=None):
    return pymysql.connect(
        host=DB_HOST,
        user=DB_USER,
        password=DB_PASSWORD,
        database=database
    )

# ================== DATABASE SETUP ==================
def create_database():
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute(f"CREATE DATABASE IF NOT EXISTS {DB_NAME}")
    conn.commit()
    cursor.close()
    conn.close()


def create_table():
    conn = get_connection(DB_NAME)
    cursor = conn.cursor()

    cursor.execute(f"""
        CREATE TABLE IF NOT EXISTS {TABLE_NAME} (
            id INT AUTO_INCREMENT PRIMARY KEY,
            flavor VARCHAR(50),
            item_type VARCHAR(50),
            name VARCHAR(255),
            ingredients TEXT,
            recipe TEXT,
            nutrition TEXT,
            fun_fact TEXT
        )
    """)

    conn.commit()
    cursor.close()
    conn.close()


def reset_table():
    conn = get_connection(DB_NAME)
    cursor = conn.cursor()
    cursor.execute(f"TRUNCATE TABLE {TABLE_NAME}")
    conn.commit()
    cursor.close()
    conn.close()


def insert_sample_data():
    conn = get_connection(DB_NAME)
    cursor = conn.cursor()

    data = [
        ("Sweet", "food", "Vanilla Cupcakes", "Flour, sugar, butter",
         "Bake at 180°C", "320 kcal", "Cupcakes are popular worldwide"),

        ("Salty", "food", "Paneer Tikka", "Paneer, spices",
         "Grill paneer", "210 kcal", "Indian starter"),

        ("Spicy", "food", "Chili Paneer", "Paneer, chili sauce",
         "Cook with sauce", "250 kcal", "Indo-Chinese dish"),

        ("Sour", "food", "Lemon Rice", "Rice, lemon",
         "Mix rice with lemon", "130 kcal", "South Indian dish"),

        ("Sweet", "beverage", "Mango Lassi", "Mango, yogurt",
         "Blend ingredients", "90 kcal", "Cooling drink")
    ]

    cursor.executemany(f"""
        INSERT INTO {TABLE_NAME}
        (flavor, item_type, name, ingredients, recipe, nutrition, fun_fact)
        VALUES (%s, %s, %s, %s, %s, %s, %s)
    """, data)

    conn.commit()
    cursor.close()
    conn.close()


def setup_database():
    create_database()
    create_table()
    reset_table()
    insert_sample_data()

# ================== DISPLAY ==================
def display_item(item):
    print("\n----------------------------")
    print(f"ID: {item[0]}")
    print(f"Flavor: {item[1]}")
    print(f"Type: {item[2]}")
    print(f"Name: {item[3]}")
    print(f"Ingredients: {item[4]}")
    print(f"Recipe: {item[5]}")
    print(f"Nutrition: {item[6]}")
    print(f"Fun Fact: {item[7]}")
    print("----------------------------")

# ================== FEATURES ==================
def view_all():
    conn = get_connection(DB_NAME)
    cursor = conn.cursor()
    cursor.execute(f"SELECT * FROM {TABLE_NAME}")
    items = cursor.fetchall()
    cursor.close()
    conn.close()

    for item in items:
        display_item(item)


def search_item():
    name = input("Enter name to search: ")
    conn = get_connection(DB_NAME)
    cursor = conn.cursor()
    cursor.execute(f"SELECT * FROM {TABLE_NAME} WHERE name LIKE %s", (f"%{name}%",))
    items = cursor.fetchall()
    cursor.close()
    conn.close()

    for item in items:
        display_item(item)


def filter_by_flavor():
    for i, f in enumerate(FLAVORS, 1):
        print(i, f)

    try:
        choice = int(input("Choose flavor: "))
        flavor = FLAVORS[choice - 1]

        conn = get_connection(DB_NAME)
        cursor = conn.cursor()
        cursor.execute(f"SELECT * FROM {TABLE_NAME} WHERE flavor = %s", (flavor,))
        items = cursor.fetchall()
        cursor.close()
        conn.close()

        for item in items:
            display_item(item)

    except:
        print("Invalid input")


def random_item():
    conn = get_connection(DB_NAME)
    cursor = conn.cursor()
    cursor.execute(f"SELECT * FROM {TABLE_NAME}")
    items = cursor.fetchall()
    cursor.close()
    conn.close()

    if items:
        display_item(random.choice(items))


def add_item():
    flavor = input("Flavor: ")
    item_type = input("Type (food/beverage): ")
    name = input("Name: ")
    ingredients = input("Ingredients: ")
    recipe = input("Recipe: ")
    nutrition = input("Nutrition: ")
    fun_fact = input("Fun fact: ")

    conn = get_connection(DB_NAME)
    cursor = conn.cursor()

    cursor.execute(f"""
        INSERT INTO {TABLE_NAME}
        (flavor, item_type, name, ingredients, recipe, nutrition, fun_fact)
        VALUES (%s,%s,%s,%s,%s,%s,%s)
    """, (flavor, item_type, name, ingredients, recipe, nutrition, fun_fact))

    conn.commit()
    cursor.close()
    conn.close()

    print("Item added!")


def delete_item():
    try:
        item_id = int(input("Enter ID to delete: "))
        conn = get_connection(DB_NAME)
        cursor = conn.cursor()
        cursor.execute(f"DELETE FROM {TABLE_NAME} WHERE id = %s", (item_id,))
        conn.commit()
        cursor.close()
        conn.close()
        print("Deleted!")
    except:
        print("Invalid ID")

# ================== MENU ==================
def menu():
    print("\n===== Gourmet Guide =====")
    print("1. View All")
    print("2. Search")
    print("3. Filter by Flavor")
    print("4. Random Recommendation")
    print("5. Add Item")
    print("6. Delete Item")
    print("7. Exit")

# ================== MAIN ==================
def main():
    setup_database()

    while True:
        menu()
        choice = input("Enter choice: ")

        if choice == "1":
            view_all()
        elif choice == "2":
            search_item()
        elif choice == "3":
            filter_by_flavor()
        elif choice == "4":
            random_item()
        elif choice == "5":
            add_item()
        elif choice == "6":
            delete_item()
        elif choice == "7":
            break
        else:
            print("Invalid choice")


if __name__ == "__main__":
    main()
