# Generated by Django 3.0.3 on 2020-05-05 20:33

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('FullThrottle', '0011_auto_20200506_0202'),
    ]

    operations = [
        migrations.RenameField(
            model_name='timestamp',
            old_name='_id',
            new_name='user_id',
        ),
    ]