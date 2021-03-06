# Generated by Django 4.0.1 on 2022-01-12 02:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('controller', '0008_processes_completed_alter_log_text_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='ipconected',
            field=models.CharField(default='', max_length=20),
        ),
        migrations.AlterField(
            model_name='log',
            name='text',
            field=models.TextField(default='operating system created at 2022-01-12 02:31:08.376464'),
        ),
        migrations.AlterField(
            model_name='user',
            name='gameip',
            field=models.CharField(default='117.200.244.84', max_length=20, unique=True),
        ),
        migrations.AlterField(
            model_name='user',
            name='gamepass',
            field=models.CharField(default='sy51h8Yz', max_length=10),
        ),
    ]
