# Generated by Django 2.2 on 2021-06-09 22:51

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('prototype_app', '0003_comment'),
    ]

    operations = [
        migrations.RenameField(
            model_name='comment',
            old_name='message',
            new_name='comment',
        ),
    ]
