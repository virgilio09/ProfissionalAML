# Generated by Django 3.2.3 on 2021-07-05 18:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('servicos', '0013_rename_ativo_servico_status'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='servico',
            name='capa',
        ),
        migrations.AlterField(
            model_name='imagem',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='', verbose_name='Adicione images do seu serviço'),
        ),
    ]
