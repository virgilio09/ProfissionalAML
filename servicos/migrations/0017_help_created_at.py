# Generated by Django 3.2.3 on 2021-07-07 16:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('servicos', '0016_help'),
    ]

    operations = [
        migrations.AddField(
            model_name='help',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, default=1),
            preserve_default=False,
        ),
    ]
