from dotenv import load_dotenv
import psycopg2
import os
from datetime import datetime

load_dotenv()

def connect_to_db():
    conn = psycopg2.connect(
        host=os.getenv('DB_HOST'),
        port=os.getenv('DB_PORT'),
        dbname=os.getenv('DB_NAME'),
        user=os.getenv('DB_USER'),
        password=os.getenv('DB_PASSWORD')
    )
    return conn


def menu_table_content():
    table = [
        (1, 'Menu 1', 'This is description of Menu 1', '2021-05-21 12:30:00', '2021-05-21 12:30:00'),
        (2, 'Menu 2', 'This is description of Menu 2', '2021-05-22 09:30:00', '2021-05-22 09:30:00'),
        (3, 'Menu 3', 'This is description of Menu 3 - has been updated!', '2021-05-23 14:00:00', '2021-05-23 16:00:00'),
        (4, 'Menu 4', 'This is description of Menu 4 - has been updated!', '2021-05-24 15:30:00', '2021-05-24 16:00:00')
    ]
    return table


def dish_table_content():
    table = [
        (1, 'Cardamom Maple Salmon', 'Dish 1 description', 20, 60, '2021-05-23 10:00:00', '2021-05-23 10:00:00', 'true', 2),
        (2, 'Spicy Pork Tenderloin with Apples and Sweet Potatoes', 'Dish 2 description', 30, 85, '2021-05-23 10:00:00', '2021-05-23 10:00:00', 'false', 2),
        (3, 'Als Burmese Chicken Curry', 'Dish 3 description', 25, 180, '2021-05-23 10:00:00', '2021-05-23 10:00:00', 'false', 2),
        (4, 'Sweet Potato and Venison Shepherds Pie', 'Dish 4 description', 31, 170, '2021-05-23 10:00:00', '2021-05-23 10:00:00', 'false', 1),
        (5, 'Gemelli Pasta with Roasted Pumpkin and Pancetta', 'Dish 5 description', 46, 55, '2021-05-23 10:00:00', '2021-05-23 10:00:00', 'true', 1),
        (6, 'Copycat Fried Chicken Sandwich', 'Dish 6 description', 28, 180, '2021-05-23 10:00:00', '2021-05-23 10:00:00', 'false', 3),
    ]
    return table


def insert_data(conn):
    cur = conn.cursor()
    try:
        print(datetime.now(), '*** Deleting existing data from "eMenu_API_dish"...')
        cur.execute("delete from \"eMenu_API_dish\"")
        
        print(datetime.now(), '*** Deleting existing data from "eMenu_API_menu"...')
        cur.execute("delete from \"eMenu_API_menu\"")

        menu_data = menu_table_content()
        print(datetime.now(), '*** Inserting data to "eMenu_API_menu"...')
        for record in menu_data:
            cur.execute(f"insert into \"eMenu_API_menu\" (id, name, description, creation_date, update_date) values {record};")
        
        dish_data = dish_table_content()
        print(datetime.now(), '*** Inserting data to "eMenu_API_dish"...')
        for record in dish_data:
            cur.execute(f"insert into \"eMenu_API_dish\" (id, name, description, price, preparation_time, creation_date, update_date, vegetarian, menu_id) values {record};")
        
        conn.commit()
        print(datetime.now(), f'*** Inserted: {len(menu_data)} items into "eMenu_API_dish".')
        print(datetime.now(), f'*** Inserted: {len(dish_data)} items into "eMenu_API_dish".')
    except Exception as e:
        print(f'*** Unexpected error: {e}')


if __name__ == '__main__':
    try:
        conn = connect_to_db()
        insert_data(conn) 
        conn.close()
    except Exception as e:
        print(f'*** Unexpected error: {e}')
    finally:
        print('*** Done! ***')