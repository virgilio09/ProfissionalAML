# Generated by Django 3.2.3 on 2021-06-29 00:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('servicos', '0009_auto_20210628_2150'),
    ]

    operations = [
        migrations.AlterField(
            model_name='endereco',
            name='cep',
            field=models.CharField(max_length=9),
        ),
    ]