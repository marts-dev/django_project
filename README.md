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
`git clone <gitlink>`
or
[Download link](#)
2. Once done with retrieving the project files, enter the project folder:
`cd django_project`
3. Install the project dependencies by running the following command:
`poetry install`
4. Change directory to `./djangobasics/djangobasics`
5. Create a **.env** file with the following contents:
> SECRET_KEY=secret key
> DATABASE_NAME=db.sqlite3

**Note:** Replace the value of secret key with output of the generate_secret.py.
You can use it by issuing: `poetry run python generate_secret.py`

6. Prepare the project database
`poetry run python manage.py migrate`
You get a result similar to the following:
![migrate result](/djangoproject/screenshots/migrate.png)

7. Create a super user for admin: `poetry run python manage.py createsuperuser`

8. Populate the database: `poetry run python manage.py loaddata statements.json`
You should get the following result:
![loaddata result](/djangoproject/screenshots/loaddata.png)

9. You may run the app using: `poetry run python manage.py runserver`

10. In your browser, you may into [localhost:8000/swagger](localhost:8000/swagger) to view the documentation