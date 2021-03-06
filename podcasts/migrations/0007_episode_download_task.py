# Generated by Django 2.0 on 2018-05-13 20:55

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('background_task', '0002_auto_20170927_1109'),
        ('podcasts', '0006_auto_20180513_0033'),
    ]

    operations = [
        migrations.AddField(
            model_name='episode',
            name='download_task',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='background_task.Task', verbose_name='Associated Download Task'),
        ),
    ]
