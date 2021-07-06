# eMenu-rest-api

### Setup:
Install all necessary modules. I recommend you to use a virtual environment.
```
pip install -r requirements.txt
```

Project uses environment variables for higher security. Create *.env* file and add following lines:
```
SECRET_KEY=django-insecure-nkum3o+ps4c@_*in8j^f9c!5_4cymjh)_=90+7xext-wdtngol
DB_NAME=
DB_USER=
DB_PASSWORD=
DB_HOST=
DB_PORT=
EMAIL_HOST=
EMAIL_PORT=
EMAIL_USER=
EMAIL_PASS=
```

Project runs on PostgreSQL by default, so environment variables with prefix DB should according to postgres db or you can modify django settings to use another database engine.

For email services provided by Google (gmail) set environment variables: `EMAIL_HOST=smtp.gmail.com` and `EMAIL_PORT=465`.

### Running project:
After configuration make migrations to the database:
```
python manage.py makemigrations
python manage.py migrate
```

Create a super user to manage django project:
```
python manage.py createsuperuser
```

Finally you can run the project:
```
python manage.py runserver
```

### Data initialization:
You can easily fill the database with sample data by running script:
```
python data_initialization.py
```

### Email report system:
To run the script which sends email reports every day at 10.00 am use command:
```
python report.py
```
