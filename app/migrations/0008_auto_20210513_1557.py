# Generated by Django 3.1.7 on 2021-05-13 07:57

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0007_journal_normally_journal'),
    ]

    operations = [
        migrations.RenameField(
            model_name='journal',
            old_name='code',
            new_name='journal',
        ),
    ]
