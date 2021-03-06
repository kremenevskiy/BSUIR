# Generated by Django 3.2.4 on 2021-06-07 23:41

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Smartphone',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255, verbose_name='Product name')),
                ('slug', models.SlugField(unique=True)),
                ('image', models.ImageField(upload_to='', verbose_name='Image')),
                ('description', models.TextField(null=True, verbose_name='Description')),
                ('price', models.DecimalField(decimal_places=2, max_digits=9, verbose_name='Price')),
                ('diagonal', models.CharField(max_length=255, verbose_name='diagonal')),
                ('display', models.CharField(max_length=255, verbose_name='display type')),
                ('resolution', models.CharField(max_length=255, verbose_name='display resolution')),
                ('accum_volume', models.CharField(max_length=255, verbose_name='accum volume')),
                ('ram', models.CharField(max_length=255, verbose_name='RAM')),
                ('sd', models.BooleanField(default=True)),
                ('sd_volume_max', models.CharField(max_length=255, verbose_name='Max volume of hdd storage')),
                ('main_cap_mp', models.CharField(max_length=255, verbose_name='Main camera')),
                ('forntal_cam_mp', models.CharField(max_length=255, verbose_name='Front camera')),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mainapp.category', verbose_name='Category')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Notebook',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255, verbose_name='Product name')),
                ('slug', models.SlugField(unique=True)),
                ('image', models.ImageField(upload_to='', verbose_name='Image')),
                ('description', models.TextField(null=True, verbose_name='Description')),
                ('price', models.DecimalField(decimal_places=2, max_digits=9, verbose_name='Price')),
                ('diagonal', models.CharField(max_length=255, verbose_name='diagonal')),
                ('display', models.CharField(max_length=255, verbose_name='display type')),
                ('processor_freq', models.CharField(max_length=255, verbose_name='Processor Frequency')),
                ('ram', models.CharField(max_length=255, verbose_name='RAM')),
                ('video', models.CharField(max_length=255, verbose_name='Video Card')),
                ('time_without_charge', models.CharField(max_length=255, verbose_name='Battery work time')),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mainapp.category', verbose_name='Category')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
