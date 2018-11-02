from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class Article(models.Model):
    title = models.CharField(default='', max_length=30)
    sTitle = models.CharField(default='', max_length=30)
    article = models.TextField(default='')
    icon = models.ImageField(default='default.png', upload_to='images/')
    image = models.ImageField(default='default.png', upload_to='images/')

    votes = models.IntegerField(default=1)
    pub_data = models.DateTimeField()
    publisher = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.title
