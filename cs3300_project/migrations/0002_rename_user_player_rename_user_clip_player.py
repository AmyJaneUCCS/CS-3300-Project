# Generated by Django 4.2.6 on 2023-11-25 01:58

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cs3300_project', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='User',
            new_name='Player',
        ),
        migrations.RenameField(
            model_name='clip',
            old_name='user',
            new_name='player',
        ),
    ]
