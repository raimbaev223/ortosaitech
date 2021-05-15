# Generated by Django 3.2.3 on 2021-05-14 07:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('machine', models.CharField(max_length=255, verbose_name='Модель машинки')),
                ('malfunction', models.CharField(max_length=255, verbose_name='Неисправность')),
                ('phone', models.CharField(max_length=20, verbose_name='Номер телефоно')),
                ('address', models.CharField(max_length=255, verbose_name='Адрес')),
                ('note', models.CharField(max_length=500, verbose_name='Примечание')),
                ('summ', models.DecimalField(decimal_places=0, max_digits=5, verbose_name='Сумма за ремонт')),
                ('costs', models.DecimalField(decimal_places=0, max_digits=5, verbose_name='Расходы на ремонт')),
            ],
        ),
    ]
