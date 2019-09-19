from django.db import models
from django.contrib.auth.models import User
from uuid import uuid4
from django.template.defaultfilters import slugify
from unidecode import unidecode
from PIL import Image
from io import BytesIO
from django.core.files.uploadedfile import InMemoryUploadedFile
import sys
import os

# Create your models here.
def upload_to(instance, filename):
    extension = filename.split('.')[-1]
    new_name = "{}.{}".format(str(uuid4()), extension)
    unique_id = instance.slug
    return os.path.join('uploads', unique_id, new_name)

class EgeNote(models.Model):
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

    faculty = models.CharField(max_length=100, choices=FACULTIES,
                               blank=False, null=True,
                               verbose_name='Faculty:')
    department = models.CharField(blank=False, null=True,
                                  max_length=200, verbose_name='Department:')
    lecture = models.CharField(blank=False, null=True,
                               max_length=200, verbose_name='Lecture:')
    page = models.CharField(blank=False, null=True,
                            max_length=200, verbose_name='Page number:')
    egenote = models.FileField(blank=False, null=True,
                               upload_to=upload_to, verbose_name="Upload note:")
    price = models.IntegerField(blank=False, null=True)
    title = models.CharField(blank=False, null=True, max_length=100)
    description = models.TextField(max_length=1000,
                                   null=True, blank=True,
                                   verbose_name="Description, Author, Content:")
    slug = models.SlugField(null=True, unique=True, editable=False)
    image = models.ImageField(upload_to=upload_to,
                              verbose_name='Media:',
                              blank=False)

    class Meta:
        verbose_name_plural = "Uploaded Notes"

    def __str__(self):
        return self.title

    def file_url(self):
        return self.egenote.url

    def get_unique_slug(self):
        number = 0
        slug = slugify(unidecode(self.title))
        new_slug = slug
        while EgeNote.objects.filter(slug=new_slug).exists():
            number += 1
            new_slug = "{}-{}".format(slug, number)
        slug = new_slug
        return slug

    def get_image(self):
        if self.image:
            return self.image.url
        else:
            return None

    def save(self, *args, **kwargs):
        if self.id is None:
            new_unique_id = str(uuid4())
            self.unique_id = new_unique_id
            self.slug = self.get_unique_slug()
        else:
            egenote = EgeNote.objects.get(slug=self.slug)
            if egenote.title != self.title:
                self.slug = self.get_unique_slug()

        #Image resize.
        if self.image:
            img = Image.open(self.image)
            output = BytesIO()
            img = img.resize((700,700))
            img.save(output, format='PNG', quality=100)
            output.seek(0)

            self.image = InMemoryUploadedFile(output,
                                              'ImageField', '%s.png' %self.image.name.split('.')[0],
                                              'image/png', sys.getsizeof(output), None)

        super(EgeNote, self).save(*args, **kwargs)