# Generated by Django 3.1.3 on 2021-04-23 09:40

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('onlinecourse', '0008_auto_20210423_0934'),
    ]

    operations = [
        migrations.RenameField(
            model_name='choice',
            old_name='is_correct',
            new_name='correct',
        ),
    ]
