#
# Run the services for development
run-services:
	docker-compose up -d

#
# Create superuser (need env var)
create-su:
	python manage.py createsuperuser --no-input