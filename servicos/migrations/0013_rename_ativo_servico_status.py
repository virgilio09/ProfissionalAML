# Generated by Django 3.2.3 on 2021-07-05 11:27

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('servicos', '0012_servico_ativo'),
    ]

    operations = [
        migrations.RenameField(
            model_name='servico',
            old_name='ativo',
            new_name='status',
        ),
    ]
