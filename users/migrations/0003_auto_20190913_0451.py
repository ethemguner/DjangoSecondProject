# Generated by Django 2.2.5 on 2019-09-13 01:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_auto_20190911_1715'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='faculty',
            field=models.CharField(blank=True, choices=[(None, 'Fakülte Seçiniz'), ('dis_hekimligi', 'Diş Hekimliği Fakültesi'), ('ezcacilik', 'Eczacılık Fakültesi'), ('edebiyat', 'Edebiyat Fakültesi'), ('egitim', 'Eğitim Fakültesi'), ('fen', 'Fen Fakültesi'), ('guzel_sanatlar', 'Güzel Sanatlar, Tasarım ve Mimarlık Fakültesi'), ('hemsirelik', 'Hemşirelik Fakültesi'), ('iibf', 'İktasi ve İdari Bilimler Fakültesi'), ('iletisim', 'İletişim Fakültesi'), ('muhendislik', 'Mühendislik Fakültesi'), ('saglik_bilimleri', 'Sağlık Bilimleri Fakültesi'), ('spor_bilimleri', 'Spor Bilimleri Fakültesi'), ('su_urunleri', 'Su Ürünleri Fakültesi'), ('tip', 'Tıp Fakültesi'), ('ziraat', 'Ziraat Fakültesi')], max_length=20, null=True, verbose_name='Fakültesi:'),
        ),
    ]
