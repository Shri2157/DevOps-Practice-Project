# Generated by Django 5.0.1 on 2024-02-14 10:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0010_alter_patient_patient_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='patient',
            name='patient_id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
    ]
