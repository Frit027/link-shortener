# Generated by Django 3.2.7 on 2021-09-22 14:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shortener', '0003_auto_20210922_1751'),
    ]

    operations = [
        migrations.AlterField(
            model_name='url',
            name='created_at',
            field=models.DateField(auto_now=True),
        ),
    ]
