# Generated by Django 5.1.6 on 2025-02-14 05:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pacientes', '0002_alter_pacientes_email_alter_pacientes_nome'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pacientes',
            name='nome',
            field=models.CharField(max_length=255),
        ),
    ]
