from django.db import models

# Create your models here.
class Base(models.Model):
    title = models.CharField(
        max_length=255,
        verbose_name="Заголовок"
    )
    descriptions = models.TextField(
        verbose_name="Описание"
    )
    logo = models.ImageField(
        upload_to='image/',
        verbose_name="Логотип сайта"
    )
    banner = models.ImageField(
        upload_to='banner/',
        verbose_name="Фото баннера"
    )
    phone = models.IntegerField(
        verbose_name="Номер телефона",
        blank=True, null=True
    )
    email = models.EmailField(
        verbose_name="Почта",
        blank=True, null=True        
    )
    instagram = models.URLField(
        verbose_name="instagram",
        blank=True, null=True        
    )
    location = models.CharField(
        max_length=255, 
        verbose_name="Адрес"
    )
    
    def __str__(self) -> str:
        return self.title
    
    class Meta:
        verbose_name = "Настройка сайта"
        verbose_name_plural = "Настройки сайта"

class Popular_category(models.Model):
    title = models.CharField(
        max_length=255,
        verbose_name="Категория блюда"
    )
    description = models.CharField(
        max_length=255,
        verbose_name="Описание блюда"
    )
    photo = models.ImageField(
        upload_to= "popular_category/",
        verbose_name="фото блюда"
    )
    def __str__(self):
        return self.title
    class Meta:
        verbose_name = "Популярная категория"
        verbose_name_plural = "Популярные категории"



class Our_chef(models.Model):
    name = models.CharField(
        max_length=255,
        verbose_name="Имя повара"
    )
    type = models.CharField(
        max_length=255,
        verbose_name="Тип повара"
    )
    photo = models.ImageField(
        upload_to='photo_chef/',
        verbose_name="фото повара"
    )
    facebook = models.URLField(
        verbose_name="Facebook - повара",
        blank=True, null=True
    )
    youtube = models.URLField(
        verbose_name="youtube - повара",
        blank=True, null=True
    )
    
    def __str__(self) -> str:
        return self.type
    
    class Meta: 
        verbose_name = "Повар"
        verbose_name_plural = "Повара"



class News(models.Model):
    title = models.CharField(
        max_length=255,
        verbose_name="Заголовок новости"
    )
    image = models.ImageField(
        upload_to='news_image/',
        verbose_name="фото новости"
    )
    author = models.CharField(
        max_length=255,
        verbose_name="Автор новости"
    )
    about = models.CharField(
        max_length=255,
        verbose_name="Краткое описание новости"
    )
    created = models.DateField(
        auto_now_add=True,
        verbose_name="Дата публикации"
    )

    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name = "Новость"
        verbose_name_plural = "Новости"

class Our_advantages(models.Model):
    title = models.CharField(
        max_length=255,
        verbose_name="Заголовок"
    )
    description = models.TextField(
        verbose_name="Описание"
    )
    def __str__(self):
        return self.title
    class Meta:
        verbose_name = "Наши преимущества"
        verbose_name_plural = "Наши преимущества"


class Specialmenu_foods(models.Model):
    name = models.CharField(
        max_length=200,
        verbose_name="Название основного блюда"      
    )
    image = models.ImageField(
        upload_to='menu_image/',
        verbose_name="Изображение блюда"
    )
    makeup1 = models.CharField(
        max_length=55,
        verbose_name="Состав блюда 1 "
    )
    makeup2 = models.CharField(
        max_length=55,
        verbose_name="Состав блюда 2"
    )
    makeup3 = models.CharField(
        max_length=55,
        verbose_name="Состав блюда 3"
    )
    price = models.IntegerField(
        verbose_name="Цена блюда"
    )
    def __str__(self) -> str:
        return self.name
    
    class Meta:
        verbose_name = "Специальное меню для А основного блюда"
        verbose_name_plural = "Специальное меню для А основных блюд"

class Specialmenu_deserts(models.Model):
    name = models.CharField(
        max_length=200,
        verbose_name="Название десерта"      
    )
    image = models.ImageField(
        upload_to='menu_image_desert/',
        verbose_name="Изображение десерта"
    )
    makeup1 = models.CharField(
        max_length=55,
        verbose_name="Состав  1 "
    )
    makeup2 = models.CharField(
        max_length=55,
        verbose_name="Состав  2"
    )
    makeup3 = models.CharField(
        max_length=55,
        verbose_name="Состав  3"
    )
    price = models.IntegerField(
        verbose_name="Цена "
    )
    def __str__(self) -> str:
        return self.name
    
    class Meta:
        verbose_name = "Специальное меню для Б десерта "
        verbose_name_plural = "Специальное меню для Б десерта"

class Specialmenu_seafood(models.Model):
    name = models.CharField(
        max_length=200,
        verbose_name="Название  блюда"      
    )
    image = models.ImageField(
        upload_to='menu_image_seafood/',
        verbose_name="Изображение блюда"
    )
    makeup1 = models.CharField(
        max_length=55,
        verbose_name="Состав блюда 1 "
    )
    makeup2 = models.CharField(
        max_length=55,
        verbose_name="Состав блюда 2"
    )
    makeup3 = models.CharField(
        max_length=55,
        verbose_name="Состав блюда 3"
    )
    price = models.IntegerField(
        verbose_name="Цена блюда"
    )
    def __str__(self) -> str:
        return self.name
    
    class Meta:
        verbose_name = "Специальное меню для В морепродукта "
        verbose_name_plural = "Специальное меню для В морепродуктов"

class Specialmenu_beverage(models.Model):
    name = models.CharField(
        max_length=200,
        verbose_name="Название напитка"      
    )
    image = models.ImageField(
        upload_to='menu_image_beverage/',
        verbose_name="Изображение напитка"
    )
    makeup1 = models.CharField(
        max_length=55,
        verbose_name="Состав  1 "
    )
    makeup2 = models.CharField(
        max_length=55,
        verbose_name="Состав  2"
    )
    makeup3 = models.CharField(
        max_length=55,
        verbose_name="Состав  3"
    )
    price = models.IntegerField(
        verbose_name="Цена "
    )
    def __str__(self) -> str:
        return self.name
    
    class Meta:
        verbose_name = "Специальное меню для Г напитка "
        verbose_name_plural = "Специальное меню для Г напитков"

        





