# Generated by Django 2.2.7 on 2020-04-27 05:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('artwork', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='user_img',
            field=models.ImageField(default=' ', upload_to='media/'),
            preserve_default=False,
        ),
    ]
