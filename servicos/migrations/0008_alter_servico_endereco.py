# Generated by Django 3.2.3 on 2021-06-25 11:58

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('servicos', '0007_auto_20210623_1914'),
    ]

    operations = [
        migrations.AlterField(
            model_name='servico',
            name='endereco',
            field=models.OneToOneField(default=1, on_delete=django.db.models.deletion.CASCADE, to='servicos.endereco'),
            preserve_default=False,
        ),
    ]
