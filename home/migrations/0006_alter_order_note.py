# Generated by Django 3.2.3 on 2021-05-15 07:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0005_maincontent'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='note',
            field=models.TextField(blank=True, max_length=500, null=True, verbose_name='Примечание'),
        ),
    ]
