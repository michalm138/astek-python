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

def send_email():
    try:
        conn = connect_to_db()
        cur = conn.cursor()

        # Collecting data
        cur.execute("select email from auth_user")
        user_emails = [item[0] for item in cur.fetchall()]
        if user_emails: 
            print(datetime.datetime.today(),'*** User emails has been fetched successfully')

        cur.execute("select id, name from \"eMenu_API_menu\"")
        menus = {item[0]:item[1] for item in cur.fetchall()}
        if user_emails: 
            print(datetime.datetime.today(),'*** Menus has been fetched successfully')
        
        yesterday_start_day = str(datetime.datetime.today().date()-datetime.timedelta(days=1)) + ' 00:00:00'
        yesterday_end_day = str(datetime.datetime.today().date()-datetime.timedelta(days=1)) + ' 23:59:59'
        cur.execute(f"select * from \"eMenu_API_dish\" where (creation_date > timestamp '{yesterday_start_day}' and creation_date < timestamp '{yesterday_end_day}') or (update_date > timestamp '{yesterday_start_day}' and update_date < timestamp '{yesterday_end_day}')")
        dishes = []
        for item in cur.fetchall():
            data = {}
            data['name'] = item[1]
            data['description'] = item[2]
            data['price'] = '$' + str(item[3])
            if item[4] == 1:
                data['preparation_time'] = str(item[4]) + ' min'
            else:
                data['preparation_time'] = str(item[4]) + ' mins'
            if item[7]:
                data['vegetarian'] = 'Yes'
            else:
                data['vegetarian'] = 'No'
            data['menu'] = menus[item[8]]
            dishes.append(data)
        if dishes:
            print(datetime.datetime.today(),'*** Dishes has been fetched successfully')
        else:
            print(datetime.datetime.today(),'*** There\'s no changes')

        # Sending email
        email_port = 465
        email_pass = os.getenv('EMAIL_PASS')
        email_context = ssl.create_default_context()
        email_message = 'Hello!\nGet yesterday\'s updates!\n\n'
        if dishes:
            for dish in dishes:
                email_message += '------------------------\n'
                email_message += 'Name: ' + dish['name'] + '\n'
                email_message += 'Description: ' + dish['description'] + '\n'
                email_message += 'Price: ' + dish['price'] + '\n'
                email_message += 'Preparation time: ' + dish['preparation_time'] + '\n'
                email_message += 'Vegetarian: ' + dish['vegetarian'] + '\n'
                email_message += 'You can find it in menu: ' + dish['menu'] + '\n'
        else:
            email_message += 'Sorry! There\'s no changes'

        with smtplib.SMTP_SSL('smtp.gmail.com', email_port, context=email_context) as server:
            server.login(os.getenv('EMAIL_USER'), os.getenv('EMAIL_PASS'))
            print(datetime.datetime.today(),'*** Sending emails...')
            for email in user_emails:
                server.sendmail(os.getenv('EMAIL_USER'), email, email_message)
            print(datetime.datetime.today(),'*** Emails have been sent successfully\n')
            server.quit()
    except:
        print(datetime.datetime.today(),'*** Error! Something went wrong...')
    finally:
        conn.close()

schedule.every().day.at("10:00").do(send_email)

if __name__ == '__main__':
    while True:
        schedule.run_pending()
        time.sleep(1)