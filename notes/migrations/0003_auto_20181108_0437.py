# Generated by Django 2.1.3 on 2018-11-08 04:37

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('notes', '0002_auto_20181108_0433'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='note',
            name='author',
        ),
        migrations.RemoveField(
            model_name='note',
            name='completed',
        ),
        migrations.RemoveField(
            model_name='note',
            name='date',
        ),
    ]
