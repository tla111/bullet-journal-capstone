# Generated by Django 3.1.5 on 2021-01-13 19:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_auto_20210113_1915'),
    ]

    operations = [
        migrations.AddField(
            model_name='blogmodel',
            name='dislikes',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='blogmodel',
            name='likes',
            field=models.IntegerField(default=0),
        ),
    ]
