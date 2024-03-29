# Generated by Django 5.0.3 on 2024-03-27 10:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('medical_facility', '0001_initial'),
        ('specialist', '0005_alter_specialist_main_specialization'),
        ('specialization', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='medicalfacility',
            name='phone_number',
            field=models.CharField(max_length=12),
        ),
        migrations.AlterField(
            model_name='medicalfacility',
            name='specialists',
            field=models.ManyToManyField(blank=True, related_name='specialist_facilities', to='specialist.specialist'),
        ),
        migrations.AlterField(
            model_name='medicalfacility',
            name='specialties',
            field=models.ManyToManyField(blank=True, related_name='medical_facilities', to='specialization.specialization'),
        ),
    ]
