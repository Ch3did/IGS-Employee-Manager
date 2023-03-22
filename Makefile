.PHONY: migrate
# Upload database
migrate:
	@python manage.py migrate

.PHONY: migrations
# Create database migrations
migrations:
	@python manage.py makemigrations

.PHONY: migrations_hard
# Create database migrations whipping any data
migrations_hard:
	@rm -r igs_employee_manager/migrations/*
	@rm db.sqlite3
	@python manage.py makemigrations

.PHONY: run
# Start Server
run:
	@python manage.py runserver 0.0.0.0:8001

.PHONY: csu
# Create Super User
csu:
	@python manage.py createsuperuser