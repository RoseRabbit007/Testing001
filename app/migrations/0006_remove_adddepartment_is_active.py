# Generated by Django 4.2.3 on 2023-07-19 09:58

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0005_remove_adddepartment_active_adddepartment_is_active'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='adddepartment',
            name='is_active',
        ),
    ]
