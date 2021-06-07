# Spider
### Simple Microservices with Django

Get all the latest updates from Africa via email from http://news.un.org/en/region/africa

#

## Technologies:
- Django
- Docker
- Celery
- Nginx
- PostgreSQL
- Rabbitmq

REST API is used for all communications.

#

## Description
Create an account in the *users* service to receive news in your inbox.
Don't use Django's default web server in production(Use an wsgi in production). The services are all in development mode.

#

## RUN
```
docker-compose up 
docker-compose down # Remove all containers
```

#
## urls
Method: `GET`

URL: `/api/v1/news/`

List of all news

---
Method: `POST`

URL: `/api/v1/register/`

Account Registeration


