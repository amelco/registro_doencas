# Generated by Django 3.1.7 on 2021-03-09 03:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cadastro', '0006_pacientes_descricao_doenca'),
    ]

    operations = [
        migrations.AlterField(
            model_name='login',
            name='senha',
            field=models.CharField(max_length=255),
        ),
    ]
