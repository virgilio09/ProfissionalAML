# Generated by Django 3.2.3 on 2021-07-07 11:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('servicos', '0015_servico_capa'),
    ]

    operations = [
        migrations.CreateModel(
            name='Help',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titulo', models.CharField(max_length=100)),
                ('text', models.TextField()),
            ],
        ),
    ]