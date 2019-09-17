from django import forms
from django.contrib.auth.models import User
from .models import Notification, PaymentNotification

class NotificationForm(forms.ModelForm):
    class Meta:
        model = Notification
        fields = ['contact', 'faculty', 'department', 'lecture', 'page', 'note']
        labels = {
            'contact':"How do we contact with you?"
        }

    def __init__(self, *args, **kwargs):
        super(NotificationForm, self).__init__(*args, **kwargs)
        for field in self.fields:
            self.fields[field].widget.attrs = {'class': 'form-control'}

class PaymentNotificationForm(forms.ModelForm):
    who_send = forms.CharField(widget=forms.TextInput, required=True, label="Who paid (account owner)")
    class Meta:
        model = PaymentNotification
        fields = ['who_send']

    def __init__(self, *args, **kwargs):
        super(PaymentNotificationForm, self).__init__(*args, **kwargs)
        for field in self.fields:
            self.fields[field].widget.attrs = {'class': 'form-control'}
