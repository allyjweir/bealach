dev-install:
	bash bin/init.sh

dev-run:
	FLASK_APP=bealach/app.py FLASK_ENV=development pipenv run bealach