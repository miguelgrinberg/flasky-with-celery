Flasky with Celery
==================

This repository contains a version of the [Flasky](https://github.com/miguelgrinberg/flasky) application featured in my O'Reilly book [Flask Web Development](http://www.flaskbook.com) that demonstrates how to run Celery.

The application is largely the same as in the book. The only change is that the sending of emails is handled by a Celery task instead of a background thread. You can look at [this commit](https://github.com/miguelgrinberg/flasky-with-celery/commit/a5bcdc4380e2858d825cf9060213d08bfa07a73a) to see exactly what changes were made.

Quick Setup
-----------

1. Clone this repository.
2. Create a virtualenv and install the requirements (`pip install requirements/dev.txt`)
3. Open a second terminal window and start a local Redis server (if you are on Linux or Mac, execute `run-redis.sh` to install and launch a private copy).
4. Open a third terminal window. Set two environment variables `MAIL_USERNAME` and `MAIL_PASSWORD` to a valid Gmail account credentials (these will be used to send emails through Gmail's SMTP server). Then start a Celery worker: `venv/bin/celery worker -A celery_worker.celery --loglevel=info`.
5. Start Flasky on your first terminal window: `venv/bin/python manage.py runserver`.
6. Go to `http://localhost:5000/` and register an account to see how the Celery background emails work!

For general details on how to integrate Celery with Flask, see my article [Using Celery with Flask](http://blog.miguelgrinberg.com/post/using-celery-with-flask).
