# Generated by Django 3.2.4 on 2021-06-09 00:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0011_auto_20210608_2357'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='status',
            field=models.CharField(choices=[('new', 'New order'), ('in_progress', 'Order in progress'), ('completed', 'Order is complated'), ('is_ready', 'Order is ready')], default='new', max_length=100, verbose_name='Order status'),
        ),
    ]
