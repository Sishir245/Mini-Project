# Generated by Django 4.0.6 on 2023-03-23 07:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('voltaire', '0004_alter_appointment_date_alter_appointment_time'),
    ]

    operations = [
        migrations.AddField(
            model_name='appointment',
            name='comment',
            field=models.TextField(default='s'),
            preserve_default=False,
        ),
    ]
