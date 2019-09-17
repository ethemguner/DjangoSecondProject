from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
import users.urls
from notification.views import send_notice, list_notifications, user_contact_info, delete_notification, payments, confirm_payment

urlpatterns = [
    path('sell-note', send_notice, name='sell-note'),
    path('notifications', list_notifications, name='recieved-sales'),
    path('user-contact', user_contact_info, name='get-contact-info'),
    path('delete-notification', delete_notification, name='delete-notification'),
    path('payment-notifications', payments, name='payment-notification'),
    path('confirm-payment', confirm_payment, name='confirm-payment'),
]