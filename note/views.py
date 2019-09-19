from django.shortcuts import render, HttpResponseRedirect, reverse, get_object_or_404
from django.contrib.auth.models import User
from .models import EgeNote
from notification.models import PaymentNotification
from notification.forms import PaymentNotificationForm
from django.contrib import messages
from .forms import NoteQueryForm
from django.db.models import Q


def list_notes(request):
    notes = EgeNote.objects.all()
    form = NoteQueryForm(data=request.GET or None)
    search = None
    if form.is_valid():
        search = form.cleaned_data.get('search', None)
        if search:
            notes = notes.filter(
                Q(title__icontains=search) | Q(lecture__icontains=search) | Q(department__icontains=search)
            )

    return render(request, 'egenote/list-notes.html',
                  context={'notes': notes, 'form': form, 'search': search, 'notes': notes})

def note_detail(request, slug):
    note = get_object_or_404(EgeNote, slug=slug)
    return render(request, 'egenote/note-detail.html', context={'note': note})

def payment_notification(request, slug):
    if not request.user.is_active:
        return HttpResponseRedirect(reverse('user-login'))
    else:
        note = get_object_or_404(EgeNote, slug=slug)
        form = PaymentNotificationForm(data=request.POST or None)
        context = {
            'note_department': note.department,
            'note_lecture': note.lecture,
            'note_description': note.description,
            'note_price': note.price,
            'note_slug': note.slug,
            'form': form
        }

        if form.is_valid():
            who_send = form.cleaned_data.get('who_send', None)
            user = get_object_or_404(User, username=request.user.username)
            paymentNotification = PaymentNotification.objects.create(user=user, bought_note=note, who_send=who_send)

            paymentNotification.save()
            msg = "<b>We've recieved your payment. You'll be available to use your note in approximately an hour.</b>"
            messages.success(request, msg, extra_tags="success")
            return HttpResponseRedirect(reverse('list-notes'))

    return render(request, 'notification/payment-notification-user.html', context=context)

def user_note_list(request):
    user = get_object_or_404(User, username=request.user.username)
    user_notes = user.profile.egenote.all()
    return render(request, 'egenote/user-note-list.html', context={'user_notes': user_notes})
