from django.contrib import admin
from .models import Notification, PaymentNotification
# Register your models here.
admin.site.register(Notification)
admin.site.register(PaymentNotification)