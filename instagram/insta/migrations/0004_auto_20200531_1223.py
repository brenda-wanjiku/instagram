# Generated by Django 3.0.6 on 2020-05-31 09:23

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('insta', '0003_image_profile'),
    ]

    operations = [
        migrations.RenameField(
            model_name='profile',
            old_name='profile',
            new_name='user',
        ),
    ]