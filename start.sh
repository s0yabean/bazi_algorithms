# start.sh

export FLASK_APP=wsgi.py
export FLASK_ENV=development
export FLASK_DEBUG=1
export APP_CONFIG_FILE=config.py
export DEV_DATABASE_URI="sqlite:////home/amr/Desktop/bazi_algorithms/bazi_algorithms/db.sqlite"
flask run
