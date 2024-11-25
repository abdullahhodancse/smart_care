# Generated by Django 5.0.6 on 2024-11-09 16:23

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('doctor', '0003_review'),
        ('patient', '0002_alter_patient_user'),
    ]

    operations = [
        migrations.CreateModel(
            name='Appointment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('appoinment_type', models.CharField(choices=[('Offline', 'Offline'), ('Online', 'Online')], max_length=20)),
                ('appointment_status', models.CharField(choices=[('Completed', 'Completed'), ('Running', 'Running'), ('Pending', 'Pending')], default='Pending', max_length=20)),
                ('symtoms', models.TextField()),
                ('cancel', models.BooleanField(default=False)),
                ('doctor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='doctor.doctor')),
                ('patient', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='patient.patient')),
                ('time', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='doctor.availabletime')),
            ],
        ),
    ]