# Generated by Django 3.2.4 on 2021-06-10 08:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0019_alter_order_buying_type'),
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
            field=models.CharField(choices=[('completed', 'Order is complated'), ('is_ready', 'Order is ready'), ('new', 'New order'), ('in_progress', 'Order in progress')], default='new', max_length=100, verbose_name='Order status'),
        ),
    ]
