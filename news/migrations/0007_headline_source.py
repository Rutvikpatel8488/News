# Generated by Django 3.0.2 on 2020-03-01 13:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0006_auto_20200301_0024'),
    ]

    operations = [
        migrations.AddField(
            model_name='headline',
            name='source',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
    ]