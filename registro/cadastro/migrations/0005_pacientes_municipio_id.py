# Generated by Django 3.1.7 on 2021-03-06 18:59

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('cadastro', '0004_auto_20210306_1855'),
    ]

    operations = [
        migrations.AddField(
            model_name='pacientes',
            name='Municipio_id',
            field=models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.CASCADE, to='cadastro.municipio'),
        ),
    ]
