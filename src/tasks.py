import html2text
from django.core.mail import send_mail
from django.template.loader import get_template

from src.celery import app


@app.task
def graphql_auth_async_email(func, args):
    """Task to send an e-mail for the graphql_auth package."""
    return func(*args)


@app.task
def send_email_from_template(template_name, contenxt={}, *args, **kwargs):
    template_content = get_template(template_name).render(**context)
    return send_mail(
        message=html2text.html2text(template_content),
        html_message=template_content,
        *args,
        **kwargs,
    )

