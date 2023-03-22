.PHONY: migrate
# Upload database
migrate:
	@python manage.py migrate

.PHONY: migrations
# Create database migrations
migrations:
	@python manage.py makemigrations

.PHONY: reset_db
# Create database migrations whipping any data
reset:
	@rm db.sqlite3
	@rm -r igs_employee_manager/migrations/0*
	@python manage.py makemigrations
	@python manage.py migrate

.PHONY: run
# Start Server
run:
	@python manage.py runserver 0.0.0.0:8001

.PHONY: csu
# Create Super User
csu:
	@python manage.py createsuperuser