# Generated by Django 2.0.6 on 2018-09-24 06:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dl_user', '0007_userregistrationrecord_department'),
    ]

    operations = [
        migrations.AddField(
            model_name='userregistrationrecord',
            name='verified',
            field=models.BooleanField(default=False),
        ),
    ]
