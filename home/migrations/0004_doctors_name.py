# Generated by Django 5.0.1 on 2024-02-13 10:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0003_remove_doctors_name_doctors_groups_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='doctors',
            name='name',
            field=models.CharField(default='DefaultName', max_length=122),
        ),
    ]
