# Generated by Django 2.2 on 2022-10-06 15:04

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('vendor', '0016_auto_20221006_1503'),
    ]

    operations = [
        migrations.RenameField(
            model_name='vendorprofile',
            old_name='total_compact',
            new_name='total_15_seater',
        ),
        migrations.RenameField(
            model_name='vendorprofile',
            old_name='total_sedan',
            new_name='total_4_seater',
        ),
        migrations.RenameField(
            model_name='vendorprofile',
            old_name='total_suv',
            new_name='total_7_seater',
        ),
    ]
