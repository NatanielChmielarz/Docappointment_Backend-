# Generated by Django 5.0.3 on 2024-03-19 11:25

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('user_app', '0003_alter_user_first_name_alter_user_last_name_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='first_name',
        ),
        migrations.RemoveField(
            model_name='user',
            name='last_name',
        ),
        migrations.RemoveField(
            model_name='user',
            name='phone_no',
        ),
    ]