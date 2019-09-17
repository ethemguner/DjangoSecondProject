# Generated by Django 2.2.5 on 2019-09-17 14:47

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0005_profile_egenote'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='profile',
            options={'verbose_name_plural': 'Profiles'},
        ),
        migrations.AlterField(
            model_name='profile',
            name='egenote',
            field=models.ManyToManyField(blank=True, null=True, to='note.EgeNote', verbose_name="User's note:"),
        ),
        migrations.AlterField(
            model_name='profile',
            name='faculty',
            field=models.CharField(blank=True, choices=[(None, 'Choose a faculty'), ('dentistry', 'Faculty of Dentistry'), ('pharmacy', 'Faculty of Pharmacy'), ('literature', 'Faculty of Literature'), ('educational', 'Faculty of Educational Sciences'), ('science', 'Faculty of Sciences'), ('arts', 'Faculty of Arts'), ('health', 'Faculty of Health Science'), ('seas', 'School of Economics and Administrative Sciences'), ('engineering', 'Faculty of Engineering'), ('medical', 'Medical Faculty'), ('law', 'Faculty of Law')], max_length=20, null=True, verbose_name='Faculty:'),
        ),
        migrations.AlterField(
            model_name='profile',
            name='phone_number',
            field=models.CharField(blank=True, max_length=10, null=True, verbose_name='Phone Number:'),
        ),
        migrations.AlterField(
            model_name='profile',
            name='user',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='User'),
        ),
    ]
