# Generated by Django 4.0.1 on 2022-01-11 22:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('controller', '0006_alter_log_text_alter_user_gameip_alter_user_gamepass_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='log',
            name='text',
            field=models.TextField(default='operating system created at 2022-01-11 22:44:35.632741'),
        ),
        migrations.AlterField(
            model_name='user',
            name='gameip',
            field=models.CharField(default='6.168.203.229', max_length=20, unique=True),
        ),
        migrations.AlterField(
            model_name='user',
            name='gamepass',
            field=models.CharField(default='GtHUafLQ', max_length=10),
        ),
    ]
