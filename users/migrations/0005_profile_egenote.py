# Generated by Django 2.2.5 on 2019-09-15 15:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('note', '0005_auto_20190915_1814'),
        ('users', '0004_auto_20190914_1717'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='egenote',
            field=models.ManyToManyField(blank=True, null=True, to='note.EgeNote', verbose_name='Kullanıcının notları:'),
        ),
    ]