# Generated by Django 5.0.1 on 2024-02-13 10:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0004_doctors_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='doctors',
            name='is_active',
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name='doctors',
            name='is_staff',
            field=models.BooleanField(default=False),
        ),
    ]
