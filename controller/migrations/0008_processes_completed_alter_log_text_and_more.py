# Generated by Django 4.0.1 on 2022-01-12 00:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('controller', '0007_alter_log_text_alter_user_gameip_alter_user_gamepass'),
    ]

    operations = [
        migrations.AddField(
            model_name='processes',
            name='completed',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='log',
            name='text',
            field=models.TextField(default='operating system created at 2022-01-12 00:45:29.106741'),
        ),
        migrations.AlterField(
            model_name='processes',
            name='logedit',
            field=models.TextField(default=''),
        ),
        migrations.AlterField(
            model_name='user',
            name='gameip',
            field=models.CharField(default='140.20.63.157', max_length=20, unique=True),
        ),
        migrations.AlterField(
            model_name='user',
            name='gamepass',
            field=models.CharField(default='BlAIxeZW', max_length=10),
        ),
    ]