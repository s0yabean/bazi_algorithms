# Bazi Algorithms App

Features:
1) See Clash/ Combinations for each person today/ weekly/ monthly/ yearly, so User knows when to engage/ avoid them
2) Pillar Interaction Predictions (Natal Against Day, Month, Year, Dynamic LP)
3) Dynamic Systems Energy Diagrams for 5 Element Visualisations

## Installation

**Installation via `requirements.txt`**:

```shell
$ git clone https://github.com/hackersandslackers/flasklogin-tutorial.git
$ cd flasklogin-tutorial
$ python3 -m venv bazi_env
$ source bazi_env/bin/activate
$ pip3 install -r requirements.txt
$ flask run
```

## Usage

Replace the values in **.env.example** with your values and rename this file to **.env**:

* `FLASK_APP`: Entry point of your application (should be `wsgi.py`).
* `FLASK_ENV`: The environment to run your app in (either `development` or `production`).
* `SECRET_KEY`: Randomly generated string of characters used to encrypt your app's data.
* `SQLALCHEMY_DATABASE_URI`: Connection URI of a SQL database.
* `LESS_BIN`: Path to your local LESS installation via `which lessc` (optional for static assets).
* `ASSETS_DEBUG`: Debug asset creation and bundling in `development` (optional).
* `LESS_RUN_IN_DEBUG`: Debug LESS while in `development` (optional).
* `COMPRESSOR_DEBUG`: Debug asset compression while in `development` (optional).


*Remember never to commit secrets saved in .env files to Github.*

-----
