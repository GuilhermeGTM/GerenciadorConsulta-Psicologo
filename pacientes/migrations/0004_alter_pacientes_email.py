# Generated by Django 5.1.6 on 2025-02-14 05:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pacientes', '0003_alter_pacientes_nome'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pacientes',
            name='email',
            field=models.EmailField(max_length=254),
        ),
    ]
