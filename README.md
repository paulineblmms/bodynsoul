# bodynsoul demo

## To test if I could make a django app that can read a csv file and load it into a database

1. `python3 -env venv env`

2. `source env/bin/activate` for mac or `env\Scripts\activate.bat` for windows

3. `pip3 install -r requirements.txt`

4. `python3 manage.py makemigrations`

5. `python3 manage.py migrate`

6. `python3 manage.py loaddata ./dataset/food.csv`

7. `python3 manage.py makemigrations`

8. `python3 manage.py migrate`

9. `python3 manage.py runserver`
