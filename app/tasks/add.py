from app import celery

@celery.task
def sum(x, y):
    print("Run periodic task")
    return x + y