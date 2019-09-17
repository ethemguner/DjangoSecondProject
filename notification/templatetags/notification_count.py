from django import template
from notification.models import Notification, PaymentNotification
register = template.Library()

@register.filter
def notifications(notice):
    allNotifications = Notification.objects.all().count()
    context = {'notifications':allNotifications}
    return context.get('notifications')

@register.filter
def paymentnotifications(notice):
    allNotifications = PaymentNotification.objects.all().count()
    context = {'notifications':allNotifications}
    return context.get('notifications')