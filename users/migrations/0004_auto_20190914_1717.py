# Generated by Django 2.2.5 on 2019-09-14 14:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0003_auto_20190913_0451'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='phone_number',
            field=models.CharField(blank=True, max_length=10, null=True, verbose_name='Telefon Numarası:'),
        ),
    ]