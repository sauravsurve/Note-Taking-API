# Generated by Django 3.0 on 2020-03-04 13:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('notes', '0002_auto_20200304_1925'),
    ]

    operations = [
        migrations.AlterField(
            model_name='note',
            name='last_updated_date',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]