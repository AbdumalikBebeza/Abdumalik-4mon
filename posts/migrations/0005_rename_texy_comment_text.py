# Generated by Django 4.1.3 on 2022-11-17 10:27

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0004_comment'),
    ]

    operations = [
        migrations.RenameField(
            model_name='comment',
            old_name='texy',
            new_name='text',
        ),
    ]