# Generated by Django 3.2.4 on 2021-06-08 07:54

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0003_somemodel'),
    ]

    operations = [
        migrations.DeleteModel(
            name='SomeModel',
        ),
    ]