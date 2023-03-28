from celery import shared_task
import os
#from django.core.mail import send_mail
from .models import Order
import smtplib
from email.mime.text import MIMEText

#TODO починить ассинхронщину и заменить почту 
@shared_task
def order_created(order_id):
    """
    Задача для отправки уведомления по электронной почте при успешном создании заказа.
    """
    order = Order.objects.get(id=order_id)
    subject = f'LogoiskZap, номер заказа: {order_id}'
    
    message = f'{order.first_name},\n\nВаш заказ принят, номер заказа: {order.id}.'
    recipient = order.email
    # mail_sent = send_mail(subject,
    #                       message,
    #                       'yra.mirocnhik2003@gmail.com',
    #                       [order.email])
    
    return send_mail(message = message,recipient= recipient, subject= subject)


def send_mail(message, recipient, subject):
    sender = 'yra.mironchik2003@gmail.com'
    password = os.environ.get('GMAIL_KEY')
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()

    try:
        server.login(sender, password)
        msg = MIMEText(message)
        msg['Subject'] = subject
        server.sendmail(sender, recipient, msg.as_string())

        return "message sent"
    except Exception as _e:
        return f'error: {_e}'
