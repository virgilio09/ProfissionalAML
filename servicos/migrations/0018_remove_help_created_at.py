# Generated by Django 3.2.3 on 2021-07-07 16:30

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('servicos', '0017_help_created_at'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='help',
            name='created_at',
        ),
    ]
