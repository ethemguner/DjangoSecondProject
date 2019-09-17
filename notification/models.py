from django.db import models
from django.contrib.auth.models import User
from note.models import EgeNote


# Create your models here.
class Notification(models.Model):
    CONTACT_TYPES = (
        (None, 'Choose an option'),
        ('wMail', 'Contact me with e-mail'),
        ('wPhone', 'Contact me with phone number')
    )

    FACULTIES = (
        (None, "Choose a faculty"),
        ('dentistry', "Faculty of Dentistry"),
        ('pharmacy', 'Faculty of Pharmacy'),
        ('literature', 'Faculty of Literature'),
        ('educational', 'Faculty of Educational Sciences'),
        ('science', 'Faculty of Sciences'),
        ('arts', 'Faculty of Arts'),
        ('health', 'Faculty of Health Science'),
        ('seas', 'School of Economics and Administrative Sciences'),
        ('engineering', 'Faculty of Engineering'),
        ('medical', 'Medical Faculty'),
        ('law', 'Faculty of Law')
    )

    user = models.ForeignKey(User, null=True, blank=False, verbose_name="User:", on_delete=models.CASCADE)
    contact = models.CharField(max_length=100, choices=CONTACT_TYPES, blank=False, null=True, verbose_name='Contact:',
                               help_text="*We'll use your saved contact information. To check, click 'My Profile'")
    faculty = models.CharField(max_length=100, choices=FACULTIES, blank=False, null=True,
                               verbose_name='Faculty:')
    department = models.CharField(blank=False, null=True, max_length=200, verbose_name='Department:',
                                  help_text="Note's department.")
    lecture = models.CharField(blank=False, null=True, max_length=200, verbose_name='Lecture:',
                               help_text="Note's lecture.")
    page = models.CharField(blank=False, null=True, max_length=200, verbose_name='Page number:')
    note = models.TextField(max_length=1000, null=True, blank=True,
                            help_text="Any information that we need to know.",
                            verbose_name="Extra note:")
    notice_date = models.DateField(auto_now_add=True, auto_now=False)

    class Meta:
        verbose_name_plural = "Selling Requests"
        ordering = ['-id']

    def __str__(self):
        return "{} adlı kullanıcıdan satış isteği!".format(self.user)

    def get_user_faculty(self):
        if self.faculty == "dentistry":
            faculty = "Faculty of Dentistry"
        elif self.faculty == "pharmacy":
            faculty = "Faculty of Pharmacy"
        elif self.faculty == "literature":
            faculty = "Faculty of Literature"
        elif self.faculty == "educational":
            faculty = "Faculty of Educational Sciences"
        elif self.faculty == "science":
            faculty = "Faculty of Sciences"
        elif self.faculty == "arts":
            faculty = "Faculty of Arts"
        elif self.faculty == "health":
            faculty = "Faculty of Health Sciences"
        elif self.faculty == "seas":
            faculty = "School of Economics and Administrative Sciences"
        elif self.faculty == "engineering":
            faculty = "Faculty of Engineering"
        elif self.faculty == "medical":
            faculty = "Medial Faculty"
        elif self.faculty == "law":
            faculty = "Faculty of Law"

        return faculty


class PaymentNotification(models.Model):
    user = models.ForeignKey(User, null=True, blank=False, verbose_name="User:", on_delete=models.CASCADE)
    bought_note = models.ForeignKey(EgeNote, null=True, blank=False, verbose_name="Want to buy:",
                                         on_delete=models.CASCADE)
    who_send = models.CharField(null=True, blank=False, verbose_name="Who paid (account owner):", max_length=100,
                                help_text="*Please enter paying account owner.*")

    class Meta:
        verbose_name_plural = "Payments"

    def __str__(self):
        return "{} has a payment notification for {} note.".format(self.user.username,
                                                                   self.bought_note.title)