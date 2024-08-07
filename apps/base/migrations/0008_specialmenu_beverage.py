# Generated by Django 5.0.6 on 2024-07-16 19:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0007_specialmenu_seafood'),
    ]

    operations = [
        migrations.CreateModel(
            name='Specialmenu_beverage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200, verbose_name='Название напитка')),
                ('image', models.ImageField(upload_to='menu_image_beverage/', verbose_name='Изображение напитка')),
                ('makeup1', models.CharField(max_length=55, verbose_name='Состав  1 ')),
                ('makeup2', models.CharField(max_length=55, verbose_name='Состав  2')),
                ('makeup3', models.CharField(max_length=55, verbose_name='Состав  3')),
                ('price', models.IntegerField(verbose_name='Цена ')),
            ],
            options={
                'verbose_name': 'Специальное меню для Г напитка ',
                'verbose_name_plural': 'Специальное меню для Г напитков',
            },
        ),
    ]
