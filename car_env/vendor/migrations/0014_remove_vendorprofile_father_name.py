# Generated by Django 2.2 on 2022-10-06 15:01

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('vendor', '0013_auto_20201112_2144'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='vendorprofile',
            name='father_name',
        ),
    ]