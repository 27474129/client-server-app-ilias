# Generated by Django 4.0.5 on 2022-07-02 10:14

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('student', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='studentfile',
            old_name='update_time',
            new_name='upload_time',
        ),
    ]
