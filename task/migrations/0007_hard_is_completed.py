# Generated by Django 5.1 on 2024-09-21 01:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('task', '0006_delete_s'),
    ]

    operations = [
        migrations.AddField(
            model_name='hard',
            name='is_completed',
            field=models.BooleanField(default=False),
        ),
    ]
