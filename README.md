# Body'N'Soul

## A Software Engineering project

## Brought to you by the Self-Believers

### Team members:

1. Ahmed Laaroussi
2. Andika Pramudya Wardana
3. Bramantyo Priyo Utomo
4. Pauline Blum Moyse

The app will be deployed via Vercel or Heroku.g

## To test if I could make a django app that can read a csv file and load it into a database

1. `python3 -env venv env`

2. `source env/bin/activate` for mac or `env\Scripts\activate.bat` for windows

3. `pip3 install -r requirements.txt`

4. `python3 manage.py loaddata ./dataset/food.csv`

5. `python3 manage.py makemigrations`

6. `python3 manage.py migrate`

7. `python3 manage.py runserver`
