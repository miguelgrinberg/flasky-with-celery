Flasky with Celery
==================

This repository contains a version of the [Flasky](https://github.com/miguelgrinberg/flasky) application featured in my O'Reilly book [Flask Web Development](http://www.flaskbook.com) that demonstrates how to run Celery.

The application is largely the same as in the book. The only change is that the sending of emails is handled by a Celery task instead of a background thread. You can look at [this commit](https://github.com/miguelgrinberg/flasky-with-celery/commit/a5bcdc4380e2858d825cf9060213d08bfa07a73a) to see exactly what changes were made.

Quick Setup
-----------

- Clone this repository.
- Create a virtualenv and install the requirements 
```
cd (repo)
virtualenv venv
cd venv
source bin/activate
cd ..
pip install -r requirements/dev.txt
```
- Run the migrations
```
python manage.py db upgrade
```
- Open a second terminal window and start a local Redis server (if you are on Linux or Mac, execute `run-redis.sh` to install and launch a private copy).
- Open a third terminal window. Set two environment variables `MAIL_USERNAME` and `MAIL_PASSWORD` to a valid Gmail account credentials (these will be used to send emails through Gmail's SMTP server). Then start a Celery worker. 
```
export MAIL_USERNAME=user@gmail.com
export MAIL_PASSWORD=password
venv/bin/celery worker -A celery_worker.celery --loglevel=info
```
- Start Flasky on your first terminal window: `venv/bin/python manage.py runserver`.
- Go to `http://localhost:5000/` and register an account to see how the Celery background emails work!

For general details on how to integrate Celery with Flask, see my article [Using Celery with Flask](http://blog.miguelgrinberg.com/post/using-celery-with-flask).
