from django.db import models

from mptt.models import MPTTModel, TreeForeignKey

# Create your models here.

class Establishments(models.Model):
    title = models.CharField(
        max_length=155, 
        verbose_name='Название' )
    subtitle = models.CharField(
        max_length=50, 
        verbose_name='короткое название')
    description = models.TextField(
        null=True, verbose_name='инфо')
    photo = models.ImageField(
        upload_to='profile_images', 
        blank=True, null=True)
    sub_photo = models.ImageField(
        upload_to='profile_images', 
        blank=True, null=True)
    location = models.CharField(
        max_length=100, 
        verbose_name='Локация')
    
    
    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name = 'Заведение'
        verbose_name_plural = 'Заведения'


class Category(MPTTModel):

    name = models.CharField(max_length=100)
    parent = TreeForeignKey(
        'self', 
        on_delete=models.CASCADE, 
        null=True, blank=True, 
        related_name='children')


    def __str__(self):
        return self.name
    

    class MPTTMeta:
        order_insertion_by = ['name']  

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'

    

class QA(models.Model):
    question = models.TextField(
        blank=True, 
        verbose_name='Вопрос')
    answer = models.TextField(
        blank=True, 
        verbose_name='Ответ')
    category = models.ForeignKey(
        'Category', 
        on_delete=models.CASCADE, 
        null=True, blank=True, 
        related_name='categories')
    
    Establishments = models.ForeignKey(
        'Establishments', 
        on_delete=models.CASCADE, 
        null=True, blank=True, 
        related_name='establishmentss')
    
    

    def str(self):
        return f'{self.question} {self.answer}'
    

    class Meta:
        verbose_name = 'Вопрос и ответ'
        verbose_name_plural = 'Вопросы и ответы'
    
    
    


