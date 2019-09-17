from django.urls import path
from .views import list_notes, note_detail, payment_notification, user_note_list

urlpatterns = [
    path('detail/<slug:slug>', note_detail , name = 'note-detail'),
    path('purchase/<slug:slug>', payment_notification , name = 'payment-page'),
    path('myNotes', user_note_list , name = 'user-note-list'),
]