# Generated by Django 5.0.1 on 2024-01-09 09:37

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mainpage', '0004_motherboard_remove_processor_cores_processor_core_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='videocard',
            name='chipset',
        ),
    ]
