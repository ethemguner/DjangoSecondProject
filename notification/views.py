from django.shortcuts import render, HttpResponseRedirect, reverse, get_object_or_404
from .models import Notification, PaymentNotification
from .forms import NotificationForm
from django.contrib import messages
from django.contrib.auth.models import User
from django.http import HttpResponseBadRequest, JsonResponse
from django.template.loader import render_to_string
from django.core.mail import send_mail
from note.models import EgeNote
from users.models import Profile
from notification.models import PaymentNotification
# Create your views here.

def send_notice(request):
    if not request.user.is_active:
        return HttpResponseRedirect(reverse('user-login'))

    form = NotificationForm(data=request.GET or None)
    user = get_object_or_404(User, username=request.user.username)

    if form.is_valid():
        contact = form.cleaned_data.get('contact')
        faculty = form.cleaned_data.get('faculty')
        department = form.cleaned_data.get('department')
        lecture = form.cleaned_data.get('lecture')
        page = form.cleaned_data.get('page')
        note = form.cleaned_data.get('note')

        notification = Notification.objects.create(user=user, contact=contact,
                                                   faculty=faculty, department=department,
                                                   lecture=lecture, page=page,
                                                   note=note)
        notification.save()

        msg = "<b>Your selling request has recieved successfully. We'll contact with you as soon as possible.</b>"
        messages.success(request, msg, extra_tags="success")
        return HttpResponseRedirect(reverse('list-notes'))
    return render(request, 'notification/notificationform.html',
                  context={'form': form})

def list_notifications(request):
    notifications = Notification.objects.all()
    return render(request, 'notification/notification-list-staff.html',
                  context={'notifications': notifications})

def user_contact_info(request):
    if not request.is_ajax():
        return HttpResponseBadRequest

    data = {'is_valid': True, 'html': '', 'user_contact': ''}
    username = request.GET.get('username', None)
    contactType = request.GET.get('contactType', None)

    user = get_object_or_404(User, username=username)

    if contactType == "wPhone":
        msg = "<b>This user wants to contact with his/her phone number. Phone number information:</b>"
        user_contact = "+90 {}".format(user.profile.phone_number)
    elif contactType == "wMail":
        msg = "<b>This user wants to contact with his/her e-mail adress. E-mail information:</b>"
        user_contact = user.email

    html = render_to_string('notification/users-contact-info.html', request=request)

    data.update({'html': html, 'user_contact': user_contact, 'msg': msg})

    return JsonResponse(data=data)


def delete_notification(request):
    if not request.is_ajax():
        return HttpResponseBadRequest

    data = {'is_valid': True}

    notification_id = request.GET.get('notification_id', None)

    notification = get_object_or_404(Notification, id=notification_id)
    notification.delete()

    return JsonResponse(data=data)

def payments(request):
    payments = PaymentNotification.objects.all()
    return render(request, 'notification/payment-notification-staff.html', context={'payments':payments})

def confirm_payment(request):
    if not request.is_ajax():
        return HttpResponseBadRequest

    data = {'is_valid':True}
    payment_id = request.GET.get('payment_id', None)
    note_id = request.GET.get('note_id', None)
    username = request.GET.get('username', None)

    user = get_object_or_404(User, username=username)
    note = get_object_or_404(EgeNote, id=note_id)

    paymentNotification = get_object_or_404(PaymentNotification, id=payment_id)
    paymentNotification.delete()

    user.profile.egenote.add(note)

    return JsonResponse(data=data)