# Generated by Django 4.1.7 on 2023-07-19 04:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('App1', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='work_shift',
            name='shift_type',
            field=models.BooleanField(choices=[('Regular Work Shift', 'Regular Work Shift '), ('Demo working Shift regular', 'Demo working Shift regular'), ('Demo working shift sheduled', 'Demo working shift sheduled')], default=True),
        ),
    ]
