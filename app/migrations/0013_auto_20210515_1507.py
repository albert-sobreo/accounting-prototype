# Generated by Django 3.1.7 on 2021-05-15 07:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0012_auto_20210515_1410'),
    ]

    operations = [
        migrations.AlterField(
            model_name='account_group',
            name='amount',
            field=models.DecimalField(blank=True, decimal_places=5, default=0.0, max_digits=24, null=True),
        ),
        migrations.AlterField(
            model_name='child_account',
            name='amount',
            field=models.DecimalField(blank=True, decimal_places=5, default=0.0, max_digits=24, null=True),
        ),
        migrations.AlterField(
            model_name='journal_entries',
            name='amount',
            field=models.DecimalField(blank=True, decimal_places=5, default=0, max_digits=24, null=True),
        ),
    ]
