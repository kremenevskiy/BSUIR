# Generated by Django 3.2.4 on 2021-06-12 17:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0045_auto_20210611_1432'),
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
            field=models.CharField(choices=[('completed', 'Order is complated'), ('is_ready', 'Order is ready'), ('in_progress', 'Order in progress'), ('new', 'New order')], default='new', max_length=100, verbose_name='Order status'),
        ),
    ]
