# Generated by Django 3.2.3 on 2021-06-29 00:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('servicos', '0008_alter_servico_endereco'),
    ]

    operations = [
        migrations.AlterField(
            model_name='servico',
            name='capa',
            field=models.ImageField(blank=True, null=True, upload_to=''),
        ),
        migrations.AlterField(
            model_name='servico',
            name='telefone01',
            field=models.CharField(max_length=15, verbose_name='Telefone 1'),
        ),
        migrations.AlterField(
            model_name='servico',
            name='telefone02',
            field=models.CharField(blank=True, max_length=15, null=True, verbose_name='Telefone 2 (Opcional)'),
        ),
    ]