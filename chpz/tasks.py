from celery import shared_task


@shared_task(bind=True, max_retries=5)
def send_welcome_email(self, username):
    try:
        from django.core.mail import send_mail
        send_mail(
            'Welcome to the Game!',
            f'Hello {username}, welcome to our game! Enjoy your experience.',
            fail_silently=False,
        )
    except Exception as exc:
        raise self.retry(exc=exc)
