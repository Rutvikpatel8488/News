# Generated by Django 3.0.2 on 2020-02-29 18:52

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0004_sheadline'),
    ]

    operations = [
        migrations.RenameField(
            model_name='sheadline',
            old_name='image',
            new_name='simage',
        ),
        migrations.RenameField(
            model_name='sheadline',
            old_name='title',
            new_name='stitle',
        ),
        migrations.RenameField(
            model_name='sheadline',
            old_name='url',
            new_name='surl',
        ),
    ]
