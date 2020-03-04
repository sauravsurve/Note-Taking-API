# Generated by Django 3.0 on 2020-03-04 14:38

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('notes', '0006_auto_20200304_2004'),
    ]

    operations = [
        migrations.AlterField(
            model_name='note',
            name='created_date',
            field=models.DateField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='note',
            name='last_updated_date',
            field=models.DateField(default=datetime.date(2020, 3, 4)),
        ),
    ]
