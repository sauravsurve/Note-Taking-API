# Generated by Django 3.0 on 2020-03-04 14:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('notes', '0012_auto_20200304_2022'),
    ]

    operations = [
        migrations.AlterField(
            model_name='note',
            name='last_updated_date',
            field=models.DateTimeField(),
        ),
    ]
