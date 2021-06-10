# Generated by Django 3.2.4 on 2021-06-10 08:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0021_auto_20210610_0844'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='buying_type',
            field=models.CharField(choices=[('delivery', 'Delivery'), ('self', 'Pickup')], default='self', max_length=100, verbose_name='Order type'),
        ),
        migrations.AlterField(
            model_name='order',
            name='status',
            field=models.CharField(choices=[('in_progress', 'Order in progress'), ('is_ready', 'Order is ready'), ('completed', 'Order is complated'), ('new', 'New order')], default='new', max_length=100, verbose_name='Order status'),
        ),
    ]
