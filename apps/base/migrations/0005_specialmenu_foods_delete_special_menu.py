# Generated by Django 5.0.6 on 2024-07-16 18:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0004_remove_special_menu_category_delete_category'),
    ]

    operations = [
        migrations.CreateModel(
            name='Specialmenu_foods',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200, verbose_name='Название основного блюда')),
                ('image', models.ImageField(upload_to='menu_image/', verbose_name='Изображение блюда')),
                ('makeup1', models.CharField(max_length=55, verbose_name='Состав блюда 1 ')),
                ('makeup2', models.CharField(max_length=55, verbose_name='Состав блюда 2')),
                ('makeup3', models.CharField(max_length=55, verbose_name='Состав блюда 3')),
                ('price', models.IntegerField(verbose_name='Цена блюда')),
            ],
            options={
                'verbose_name': 'Специальное меню',
                'verbose_name_plural': 'Специальное меню',
            },
        ),
        migrations.DeleteModel(
            name='Special_menu',
        ),
    ]
