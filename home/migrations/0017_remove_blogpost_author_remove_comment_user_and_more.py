# Generated by Django 4.0.6 on 2022-07-13 20:10

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0016_profile_phone_no'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='blogpost',
            name='author',
        ),
        migrations.RemoveField(
            model_name='comment',
            name='user',
        ),
        migrations.DeleteModel(
            name='Profile',
        ),
    ]
