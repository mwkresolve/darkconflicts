# Generated by Django 4.0.1 on 2022-01-17 23:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('controller', '0015_alter_hackeddatabase_iphacked_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='gameip',
            field=models.CharField(default='45.118.224.182', max_length=20, unique=True),
        ),
        migrations.AlterField(
            model_name='user',
            name='gamepass',
            field=models.CharField(default='', max_length=10),
        ),
        migrations.AlterField(
            model_name='user',
            name='log',
            field=models.TextField(default='operating system created at 2022-01-17 23:44:47.733533'),
        ),
    ]