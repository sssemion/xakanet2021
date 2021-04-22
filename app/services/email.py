from threading import Thread

from flask_mail import Message


def send_email(subject, sender, recipients, text_body, html_body):

    return Thread(target=_send_async_email, args=(subject, sender, recipients, text_body,
                                                  html_body)).start()


def _send_async_email(subject, sender, recipients, text_body, html_body):
    from app import app
    with app.app_context():
        msg = Message(subject, sender=sender, recipients=recipients)
        msg.body = text_body
        msg.html = html_body
        from app import mail
        mail.send(msg)
