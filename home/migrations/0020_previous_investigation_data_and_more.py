# Generated by Django 5.0.1 on 2024-04-05 08:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0019_diagnosis_data'),
    ]

    operations = [
        migrations.CreateModel(
            name='previous_investigation_data',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('patient_id', models.CharField(max_length=122)),
                ('patient_name', models.CharField(max_length=122)),
                ('Details', models.CharField(max_length=1222)),
            ],
        ),
        migrations.AlterField(
            model_name='diagnosis_data',
            name='Details',
            field=models.CharField(max_length=1222),
        ),
    ]
