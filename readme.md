# Capstone Project

## Getting Started

### Heroku Link

https://capstone-project-nanodegree.herokuapp.com

### Installing Dependencies

#### Python 3.7

Follow instructions to install the latest version of python for your platform in the [python docs](https://docs.python.org/3/using/unix.html#getting-and-installing-the-latest-version-of-python)

#### Virtual Environment

We recommend working within a virtual environment whenever using Python for projects. This keeps your dependencies for each project separate and organized. Instructions for setting up a virtual environment for your platform can be found in the [python docs](https://packaging.python.org/guides/installing-using-pip-and-virtual-environments/)

#### PIP Dependencies

Once you have your virtual environment setup and running, install dependencies by naviging to the `/starter` directory and running:

```bash
pip install -r requirements.txt
```

This will install all of the required packages we selected within the `requirements.txt` file.

##### Key Dependencies

- [Flask](http://flask.pocoo.org/) is a lightweight backend microservices framework. Flask is required to handle requests and responses.

- [SQLAlchemy](https://www.sqlalchemy.org/) and [Flask-SQLAlchemy](https://flask-sqlalchemy.palletsprojects.com/en/2.x/) are libraries to handle the lightweight sqlite database. Since we want you to focus on auth, we handle the heavy lift for you in `./src/database/models.py`. We recommend skimming this code first so you know how to interface with the Drink model.

- [jose](https://python-jose.readthedocs.io/en/latest/) JavaScript Object Signing and Encryption for JWTs. Useful for encoding, decoding, and verifying JWTS.

## Running the server

From within the `./starter` directory first ensure you are working using your created virtual environment.

Each time you open a new terminal session, run:

```bash
export FLASK_APP=app.py;
```

To run the server, execute:

```bash
flask run --reload
```

The `--reload` flag will detect file changes and restart the server automatically.


### Setup Auth0

You will find a link to in the '/' route that wil lead you to Auth0 authentication page. I have prepared three users with three different roles in the file 'Users data.txt'. You'll also find the JWT tokens needed to access all the pages. In case the tokens were expired; you can use the credentials in the file to regenerate them.

### Postman test

You will find a JSON collection in the file 'Capstone.postman_collection.json' with tests for each role.

###

Endpoints
GET '/actors'
GET '/movies'
POST '/actors'
POST '/movies'
PATCH '/actors/<id>'
PATCH '/movies/<id>'
DELETE '/actors/<id>'
DELTE '/movies/<id>'

GET '/actors'
- Fetches an array filled with JSON of actors with thier informations.
- Request Arguments: None
- Returns: JSON of actors Array. 

GET '/movies'
- Fetches an JSON of movies array.
- Request Arguments: None.
- Returns: array filled with JSON of movies: 

POST '/actors'
- Creates a new actor.
- Request Arguments: a JSON with the following from: {'name': String, 'age': Int, 'gender': String}
- Returns:  A variable "success" that indicates if the request passed or failed

POST '/movies'
- Creates a new movie.
- Request Arguments: a JSON with the following form: {'title': String, 'release data': Date}
- Returns: A variable "success" that indicates if the request passed or failed. The request fails in the case of a missing argument.

PATCH '/actors/<id>'
- Edits an exitsting actor.
- Request Arguments: 
-The id of the actor.
-JSON with the follwing form {'name': String, 'age': Int, 'gender': String}
- Returns:  A variable "success" that indicates if the request passed or failed

PATCH '/moives/<id>'
- Edits an existing movie.
- Request Arguments: 
-The ID of the movie.
-JSON with the following form: {'title': String, 'release data': Date}
- Returns: A "Success" variable that indicates if the request have been fulfilled or not.

DELETE '/actors/<id>'
-Deletes an existing actor.
-Request Arguments: The id of the actor to be deleted
-Returns:  A variable "success" that indicates if the request passed or failed

DELETE '/movies/<id>'
-Deletes an existing movie.
-Request Arguments: The id of the actor to be movie
-Returns:  A variable "success" that indicates if the request passed or failed


## Testing
To run the tests, run
```
dropdb casting_agnecy_test
createdb casting_agency_test
python test_app.py
```
`