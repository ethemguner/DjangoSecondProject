# Generated by Django 2.2.5 on 2019-09-15 17:57

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('note', '0005_auto_20190915_1814'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('notification', '0004_auto_20190913_0451'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='notification',
            options={'ordering': ['-id'], 'verbose_name_plural': 'Satış Bildirimleri'},
        ),
        migrations.CreateModel(
            name='PaymentNotification',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('who_send', models.CharField(help_text='*Ödemeyi yapan hesap sahibinin ad ve soyadını giriniz.*', max_length=100, null=True, verbose_name='Ödemeyi yapan kişi:')),
                ('bought_note', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='note.EgeNote', verbose_name='Satın almak istediği not:')),
                ('user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Kullanıcı:')),
            ],
            options={
                'verbose_name_plural': 'Ödeme Bildirimleri',
            },
        ),
    ]
