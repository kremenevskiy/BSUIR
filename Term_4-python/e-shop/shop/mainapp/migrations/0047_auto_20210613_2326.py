# Generated by Django 3.2.4 on 2021-06-13 23:26

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0046_auto_20210612_1707'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='buying_type',
            field=models.CharField(choices=[('self', 'Pickup'), ('delivery', 'Delivery')], default='self', max_length=100, verbose_name='Order type'),
        ),
        migrations.AlterField(
            model_name='order',
            name='customer',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='related_orders', to='mainapp.customer', verbose_name='Customer'),
        ),
        migrations.AlterField(
            model_name='order',
            name='status',
            field=models.CharField(choices=[('is_ready', 'Order is ready'), ('new', 'New order'), ('in_progress', 'Order in progress'), ('completed', 'Order is complated')], default='new', max_length=100, verbose_name='Order status'),
        ),
    ]
