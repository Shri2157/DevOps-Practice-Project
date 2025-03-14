# Generated by Django 5.0.1 on 2024-04-05 07:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0017_clinical_summary_data_patient_id_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='general_examination_data',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('patient_id', models.CharField(max_length=122)),
                ('patient_name', models.CharField(max_length=122)),
                ('Blood_Pressure', models.CharField(max_length=122)),
                ('Temperature', models.CharField(max_length=122)),
                ('Height', models.CharField(max_length=122)),
                ('Sugar_level', models.CharField(max_length=122)),
            ],
        ),
    ]
