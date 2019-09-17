from django.db import models
from django.contrib.auth.models import User
from note.models import EgeNote

class Profile(models.Model):
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

    user = models.OneToOneField(User, null=True, blank=False, verbose_name="User", on_delete=models.CASCADE)
    faculty = models.CharField(choices=FACULTIES, blank=True, null=True, max_length=20, verbose_name='Faculty:')
    phone_number = models.CharField(max_length=10, verbose_name='Phone Number:', blank=True, null=True)
    egenote = models.ManyToManyField(EgeNote, null=True, blank=True, verbose_name="User's note:")

    class Meta:
        verbose_name_plural = "Profiles"

    def __str__(self):
        return self.user.username

    def get_faculty(self):
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

    def user_email(self):
        return self.user.email