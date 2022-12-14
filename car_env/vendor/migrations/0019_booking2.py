# Generated by Django 2.2 on 2022-10-07 13:26

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('vendor', '0018_auto_20221007_1045'),
    ]

    operations = [
        migrations.CreateModel(
            name='booking2',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pick_up', models.CharField(max_length=50)),
                ('drop_off', models.CharField(max_length=50)),
                ('distance', models.CharField(max_length=5)),
                ('price', models.CharField(max_length=7)),
                ('name_of_person', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='vendor.vendorprofile')),
            ],
        ),
    ]
