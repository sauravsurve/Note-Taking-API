# Generated by Django 3.0 on 2020-03-04 14:44

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('notes', '0007_auto_20200304_2008'),
    ]

    operations = [
        migrations.AlterField(
            model_name='note',
            name='last_updated_date',
            field=models.DateField(default=django.utils.timezone.now),
        ),
    ]
