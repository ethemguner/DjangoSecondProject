# Generated by Django 2.2.5 on 2019-09-14 23:36

from django.db import migrations, models
import note.models


class Migration(migrations.Migration):

    dependencies = [
        ('note', '0003_auto_20190914_2359'),
    ]

    operations = [
        migrations.AddField(
            model_name='egenote',
            name='image',
            field=models.ImageField(help_text='Bu alanda fotoğraf yükleyebilirsiniz.', null=True, upload_to=note.models.upload_to, verbose_name='Medya:'),
        ),
    ]
