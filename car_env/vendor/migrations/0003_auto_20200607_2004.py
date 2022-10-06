# Generated by Django 2.2 on 2020-06-07 20:04

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('vendor', '0002_auto_20200607_1043'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='vendorprofile',
            name='account_holder_name',
        ),
        migrations.RemoveField(
            model_name='vendorprofile',
            name='account_no',
        ),
        migrations.RemoveField(
            model_name='vendorprofile',
            name='account_type',
        ),
        migrations.RemoveField(
            model_name='vendorprofile',
            name='bank_address',
        ),
        migrations.RemoveField(
            model_name='vendorprofile',
            name='bank_name',
        ),
        migrations.RemoveField(
            model_name='vendorprofile',
            name='ifsc',
        ),
        migrations.AddField(
            model_name='vendorprofile',
            name='rejection_reason',
            field=models.TextField(default=1),
            preserve_default=False,
        ),
        migrations.CreateModel(
            name='bank_detail',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('account_holder_name', models.CharField(max_length=50)),
                ('account_no', models.IntegerField()),
                ('bank_name', models.CharField(max_length=50)),
                ('account_type', models.CharField(choices=[('C', 'Current'), ('S', 'Saving')], max_length=1)),
                ('ifsc', models.CharField(max_length=20)),
                ('bank_address', models.CharField(max_length=200)),
                ('vendor', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='vendor.vendorprofile')),
            ],
        ),
    ]