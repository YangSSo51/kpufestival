# Generated by Django 2.2.3 on 2019-09-22 13:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('intro', '0009_auto_20190920_1526'),
    ]

    operations = [
        migrations.AddField(
            model_name='intro',
            name='check',
            field=models.IntegerField(default=0),
        ),
    ]
