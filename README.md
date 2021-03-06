# Agile Principles and Values REST API
REST API for displaying Agile Principles and Values
implemented using Django Rest Framework.

## Getting Started
### Requirements
1. [Python 3.8](https://wiki.python.org/moin/BeginnersGuide/Download)
2. [Poetry](https://python-poetry.org/docs/)

## Setting up the project locally
After accomplishing the requirements above, you may proceed with the following steps in you terminal:
1. Clone the project repository from github:
`git clone https://github.com/marts-dev/django_project.git`
or
[Download link](https://github.com/marts-dev/django_project/archive/master.zip)
2. Once done with retrieving the project files, enter the project folder:
`cd django_project`
3. Install the project dependencies by running the following command:
`poetry install`
4. Change directory to **./djangobasics/djangobasics**<br>
`cd djangobasics\djangobasics`
5. Create a **.env** file with the following contents:
> SECRET_KEY=secret key<br>
> DATABASE_NAME=db.sqlite3

**Note:** Replace the value of secret key with the output of the **generate_secret.py**.
You can use it by issuing: `poetry run python generate_secret.py`

6. Prepare the project database, go back one directory level using `cd ..` then execute the following:<br>
`poetry run python manage.py migrate`<br>
You get a result similar to the following:
![migrate result](/djangobasics/screenshots/migrate.png)

7. Create a super user for admin: `poetry run python manage.py createsuperuser`
<br>**Note:** Supply the appropriate info based on the prompt

8. Populate the database: `poetry run python manage.py loaddata statements.json`
You should get the following result:
![loaddata result](/djangobasics/screenshots/loaddata.png)

9. You may run the app using: `poetry run python manage.py runserver`

10. In your browser, you may go to [localhost:8000/swagger](localhost:8000/swagger), to view the documentation

## Running the development tools
Before runing any of the development tools like pytest, make sure you are inside **.\django_project\djangobasics** directory **manage.py** resides.
<br>
- **Pytest** - to run your tests<br>
`poetry run pytest`
<br>
You may also select specific test sets: [`statementmodels`, `agilelinks`, `getmethods`, `writemethods`]<br>
Ex: `poetry run pytest -m getmethods`<br>
- **mypy** - to type hint your code<br>
`poetry run mypy agilelist`
- **black** - to format your code<br>
`poetry run black agilelist`
- **flake8** - to check pep8 rules<br>
`poetry run flake8 agilelist`
- **bandit** - a tool designed to find common security issues in Python code<br>
`poetry run bandit -r agilelist`