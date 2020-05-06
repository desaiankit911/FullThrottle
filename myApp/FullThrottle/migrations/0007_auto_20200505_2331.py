# Generated by Django 3.0.3 on 2020-05-05 18:01

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('FullThrottle', '0006_auto_20200505_2309'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='timestamp',
            options={'verbose_name_plural': 'timeStamp'},
        ),
        migrations.AlterModelOptions(
            name='userdata',
            options={'verbose_name_plural': 'UserData'},
        ),
        migrations.AddField(
            model_name='timestamp',
            name='tz',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.SET_DEFAULT, to='FullThrottle.UserData', verbose_name='UserData'),
        ),
    ]
