from src.celery import app


@app.task
def graphql_auth_async_email(func, args):
    """Task to send an e-mail for the graphql_auth package."""
    return func(*args)

