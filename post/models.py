from django.db import models

# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=50,verbose_name='Başlık')
    content = models.TextField(verbose_name='İçerik')
    publishedDate = models.DateField(verbose_name='Ekleme Tarihi')

    def __str__(self):
        return self.title
