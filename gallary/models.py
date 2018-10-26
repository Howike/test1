from django.db import models

# Create your models here.


class Gallary(models.Model):
    description = models.CharField(default='在这里描述', max_length=100)
    image = models.ImageField(default='default.png', upload_to='images/')
    title = models.CharField(default='标题', max_length=50)
    text = models.TextField(default='正文')

    def __str__(self):
        return self.title

