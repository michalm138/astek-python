import psycopg2
from dotenv import load_dotenv
import os
import smtplib, ssl
import datetime
import schedule
import time

load_dotenv()

def connect_to_db():
    conn = psycopg2.connect(
        dbname=os.getenv('DB_NAME'),
        user=os.getenv('DB_USER'),
        password=os.getenv('DB_PASSWORD'),
        host=os.getenv('DB_HOST'),
        port=os.getenv('DB_PORT')
    )

    return conn


def get_emails(connection):
    try:
        cur = connection.cursor()
        cur.execute("select email from auth_user")
        user_emails = [item[0] for item in cur.fetchall()]
        if user_emails: 
            print(datetime.datetime.today(),'*** User emails have been fetched successfully')
        return user_emails
    except Exception as e:
        print(datetime.datetime.today(),'*** Error:', e)


def get_dishes(connection):
    try:
        yesterday = str(datetime.datetime.today().date()-datetime.timedelta(days=1))
        yesterday_start = yesterday + ' 00:00:00'
        yesterday_end = yesterday + ' 23:59:59'
        dishes = []

        cur = connection.cursor()
        cur.execute(f"""
        select emad.name, emad.description, emad.price, emad.preparation_time, emad.vegetarian, emam.name, emad.creation_date, emad.update_date 
        from "eMenu_API_dish" emad
        inner join "eMenu_API_menu" emam on emad.menu_id = emam.id
        where (emad.creation_date > timestamp '{yesterday_start}' and emad.creation_date < timestamp '{yesterday_end}') or (emad.update_date > timestamp '{yesterday_start}' and emad.update_date < timestamp '{yesterday_end}')
        """)
        for field in cur.fetchall():
            data = {}
            data['name'] = field[0]
            data['description'] = field[1]
            data['price'] = field[2]
            data['preparation_time'] = field[3]
            data['vegetarian'] = field[4]
            data['menu'] = field[5]
            dishes.append(data)
        if dishes: 
            print(datetime.datetime.today(),'*** Dishes have been fetched successfully')
        else:
            print(datetime.datetime.today(),'*** Dishes have no changes')
        return dishes
    except Exception as e:
        print(datetime.datetime.today(),'*** Error:', e)


def send_emails(user_emails, email_host, email_port, email_user, email_pass, email_context, email_message):
    try:
         with smtplib.SMTP_SSL(email_host, email_port, context=email_context) as server:
            server.login(email_user, email_pass)
            print(datetime.datetime.today(),'*** Sending emails...')
            for email in user_emails:
                server.sendmail(email_user, email, email_message)
            print(datetime.datetime.today(),'*** Emails have been sent successfully')
            server.quit()
    except Exception as e:
        print(datetime.datetime.today(),'*** Error:', e)
        

def main():
    try:
        conn = connect_to_db()

        user_emails = get_emails(conn)
        dishes = get_dishes(conn)

        conn.close()

        email_host = os.getenv('EMAIL_HOST')
        email_port = os.getenv('EMAIL_PORT')
        email_user = os.getenv('EMAIL_USER')
        email_pass = os.getenv('EMAIL_PASS')
        email_context = ssl.create_default_context()
        email_message = 'Hello!\nGet yesterday\'s updates!\n\n'
        if dishes:
            for dish in dishes:
                email_message += '------------------------\n'
                email_message += 'Name: ' + dish['name'] + '\n'
                email_message += 'Description: ' + dish['description'] + '\n'
                email_message += 'Price: $' + str(dish['price']) + '\n'
                email_message += 'Preparation time: ' + str(dish['preparation_time']) + ' min\n'
                if dish['vegetarian']:
                    email_message += 'Vegetarian: Yes\n'
                else:
                    email_message += 'Vegetarian: No\n'
                email_message += 'You can find it in menu: ' + dish['menu'] + '\n'
        else:
            email_message += 'Sorry! There\'s no changes'

        send_emails(user_emails, email_host, email_port, email_user, email_pass, email_context, email_message)
        print('*** Done! ***\n')
    except Exception as e:
        print(datetime.datetime.today(),'*** Error:', e)


schedule.every().day.at("10:00").do(main)

if __name__ == '__main__':
    while True:
        schedule.run_pending()
        time.sleep(1)