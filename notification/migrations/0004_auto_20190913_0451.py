# Generated by Django 2.2.5 on 2019-09-13 01:51

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('notification', '0003_auto_20190911_1842'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='notification',
            options={'ordering': ['-id'], 'verbose_name_plural': 'Bildirimler'},
        ),
    ]