import time
from datetime import datetime, timedelta

from django.conf import settings
from django.core.mail import EmailMessage

from celery import shared_task

from django.template.loader import render_to_string

from core.models import Subscriber
from product.models import Product
from django.db.models import Count


# @shared_task
# def send_mail_to_subscribers():
#     subscribers = Subscriber.objects.distinct('email').values_list('email', flat=True)

#     last_week = datetime.today() - timedelta(days=7)
#     products = Product.objects.filter(created_at__gte=last_week).annotate(num_rev=Count('reviews')) \
# .order_by('-num_rev')[:3]


#     body = render_to_string('email-subscribers.html', context={
#         'products': products,
#         'SITE_ADDRESS': settings.SITE_ADDRESS
#     })
#     msg = EmailMessage(subject='New Products from PAVSHOP', body=body,
#                        from_email=settings.EMAIL_HOST_USER, to=subscribers, )
#     msg.content_subtype = 'html'
#     msg.send()


@shared_task
def send_mail_to_subscribers():
    subscribers = Subscriber.objects.distinct('email').values_list('email', flat=True)

    last_month = datetime.today() - timedelta(days=30)
    products = Product.objects.filter(created_at__gte=last_month).annotate(num_rev=Count('reviews')) \
.order_by('-num_rev')[:5]

    body = render_to_string('email-subscribers.html', context={
        'products': products,
        'SITE_ADDRESS': settings.SITE_ADDRESS
    })
    msg = EmailMessage(subject='New Products from PAVSHOP', body=body,
                       from_email=settings.EMAIL_HOST_USER, to=subscribers, )
    msg.content_subtype = 'html'
    msg.send()
