from django.contrib import admin
from .models import Notification, PaymentNotification, CancelPayment
# Register your models here.
admin.site.register(Notification)
admin.site.register(PaymentNotification)
admin.site.register(CancelPayment)