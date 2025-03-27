# Generated by Django 5.1.5 on 2025-03-27 00:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('citas', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='appointment',
            name='type',
        ),
        migrations.AddField(
            model_name='appointment',
            name='motivo',
            field=models.CharField(default='Consulta general', max_length=255),
        ),
        migrations.AddField(
            model_name='appointment',
            name='time',
            field=models.TimeField(default='12:00'),
        ),
        migrations.AlterField(
            model_name='appointment',
            name='date',
            field=models.DateField(),
        ),
    ]
