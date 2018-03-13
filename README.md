[![License: CC BY-NC-ND 4.0](https://licensebuttons.net/l/by-nc-nd/4.0/80x15.png)](https://creativecommons.org/licenses/by-nc-nd/4.0/)

# gitar
guitar chords and tabs

# install requirements
pip install -r requirements.txt

# run server
1- go to the directory with "manage.py"

2- only the first time you are running the project, create a mysql database named "gitar" manually. Enter your password where it says "your password" in gitar/gitar/settings.py

3- only the first time you are running the project after creating the database:

>python manage.py migrate

3- start the server

>python manage.py runserver

# populate empty database
1- go to the directory with "manage.py"

2- run python shell with django
>python manage.py shell

3- run this line of code:
>exec(open("populate_database.py", "r").read())





