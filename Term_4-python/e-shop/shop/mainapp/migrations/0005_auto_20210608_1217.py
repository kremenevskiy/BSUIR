# Generated by Django 3.2.4 on 2021-06-08 12:17

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0004_delete_somemodel'),
    ]

    operations = [
        migrations.RenameField(
            model_name='smartphone',
            old_name='forntal_cam_mp',
            new_name='frontal_cam_mp',
        ),
        migrations.RenameField(
            model_name='smartphone',
            old_name='main_cap_mp',
            new_name='main_cam_mp',
        ),
    ]
