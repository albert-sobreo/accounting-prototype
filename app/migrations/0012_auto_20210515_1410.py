# Generated by Django 3.1.7 on 2021-05-15 06:10

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0011_auto_20210513_2155'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='journal',
            options={'verbose_name': 'Journal', 'verbose_name_plural': 'Journals'},
        ),
        migrations.AlterModelOptions(
            name='journal_entries',
            options={'verbose_name': 'Journal Entry', 'verbose_name_plural': 'Journal Entries'},
        ),
    ]
