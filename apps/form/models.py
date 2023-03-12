from django.db import models
from apps.project.models import models

# Create your models here.

class Form(models.Model):
    name = models.CharField(
        max_length=25, verbose_name='Имя')
    email = models.EmailField(
        max_length=100, verbose_name='Почта')
    establishments = models.ForeignKey(
        'project.Establishments', 
        on_delete=models.CASCADE, 
        null=True, blank=True, 
        related_name='form_establishmentss', 
        verbose_name='Здания')
    text_form = models.TextField(verbose_name='форма текста')
    data_time = models.DateTimeField()

    def __str__(self):
        return self.establishments
    
    class Meta:
        verbose_name = 'Форма'
        verbose_name_plural = 'Формы'


class FormHistory(models.Model):
    form = models.ForeignKey(
        'Form', on_delete=models.CASCADE, 
        related_name='form_history', 
        verbose_name='Мои запросы')
    sent_time = models.DateTimeField(auto_now_add=True)
    establishments = models.ForeignKey(
        'project.Establishments', 
        on_delete=models.CASCADE, 
        null=True, blank=True, 
        related_name='form_history_establishmentss', 
        verbose_name='Здания')


    
    class Meta:
        verbose_name = 'Мой запрос'
        verbose_name_plural = 'Мои запросы'



