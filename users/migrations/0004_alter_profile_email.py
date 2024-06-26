# Generated by Django 4.2.11 on 2024-05-07 05:18

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0003_profile_email'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='email',
            field=models.EmailField(default='', max_length=254, validators=[django.core.validators.RegexValidator(code='invalid_email', message='Please enter a valid email address', regex='^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\\.[a-zA-Z]{2,}$')]),
        ),
    ]
