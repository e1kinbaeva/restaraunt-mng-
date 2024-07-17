from django.db import models

# Create your models here.

class Translate(models.Model):
    title = models.CharField(
        max_length=255,
        verbose_name="Заголовок банера"
    )
    hotline = models.CharField(
        max_length=255,
        verbose_name="Горячая линия"
    )
    our_location = models.CharField(
        max_length=255,
        verbose_name="Наша локация"
    )
    email = models.CharField(
        max_length=255,
        verbose_name="Почта"
    )
    def __str__(self) -> str:
        return f'{self.title} - {self.hotline}'
    
    class Meta:
        verbose_name = 'Перевод страницы контакты'
        verbose_name_plural = "Перевод страницы контакты"   
        