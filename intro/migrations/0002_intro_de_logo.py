# Generated by Django 2.2.3 on 2019-09-11 11:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('intro', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='intro',
            name='de_logo',
            field=models.FileField(default='https://image.flaticon.com/icons/svg/149/149852.svg', upload_to='department'),
        ),
    ]