# Generated by Django 5.0.3 on 2024-03-23 14:48

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('specialist', '0004_alter_reviews_description'),
        ('specialization', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='specialist',
            name='main_specialization',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='specialist_specializations', to='specialization.specialization'),
        ),
    ]