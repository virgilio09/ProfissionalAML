# Generated by Django 3.2.3 on 2021-07-05 19:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('servicos', '0014_auto_20210705_1535'),
    ]

    operations = [
        migrations.AddField(
            model_name='servico',
            name='capa',
            field=models.ImageField(blank=True, null=True, upload_to=''),
        ),
    ]
