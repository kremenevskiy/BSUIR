# Generated by Django 3.2.4 on 2021-06-10 08:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0023_auto_20210610_0855'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='status',
            field=models.CharField(choices=[('in_progress', 'Order in progress'), ('new', 'New order'), ('is_ready', 'Order is ready'), ('completed', 'Order is complated')], default='new', max_length=100, verbose_name='Order status'),
        ),
    ]
