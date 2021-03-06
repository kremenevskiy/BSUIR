# Generated by Django 3.2.4 on 2021-06-10 14:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0042_alter_order_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='status',
            field=models.CharField(choices=[('is_ready', 'Order is ready'), ('new', 'New order'), ('completed', 'Order is complated'), ('in_progress', 'Order in progress')], default='new', max_length=100, verbose_name='Order status'),
        ),
    ]
