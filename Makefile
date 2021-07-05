.PHONY: adresse
adresse:
	echo "https://londonappdeveloper.com/deploying-django-to-google-app-engine-using-docker/"

.PHONY: login
login:
	docker-compose -f docker-compose-deploy.yml run --rm gcloud sh -c "gcloud auth login"

.PHONY: migrate
migrate:
	docker-compose run --rm app sh -c "python manage.py makemigrations"
	docker-compose run --rm app sh -c "python manage.py migrate"

.PHONY: superuser
superuser:
	docker-compose run --rm app sh -c "python manage.py createsuperuser"

.PHONY: addpro
addpro:
	docker-compose run --rm app sh -c "django-admin startproject app ."

.PHONY: addapp
addapp:
	docker-compose run --rm app sh -c "python manage.py startapp demo"

.PHONY: up
up:
	docker-compose up

.PHONY: dbdroit
dbdroit:
	echo "must be done by the super user"
	echo "to permit web access to the data base"
	chown wwwrun app
	chown wwwrun app/db.sqlite3
	echo "i will still need to keep acces"
	echo "to the data base as an user"
	chmod g+w app
	chmod g+w app/db.sqlite3

.PHONY: collect
collect:
	mkdir -p static/admin
	docker-compose run --rm app sh -c "python manage.py collectstatic"

.PHONY: deploy
deploy: collect
	docker-compose -f docker-compose-deploy.yml run --rm gcloud sh -c "gcloud app deploy --project pydjango"
