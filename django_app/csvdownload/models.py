from django.db import models

class Post(models.Model):
    """役職マスタ"""
    name = models.CharField('役職名', max_length=50)

    def __str__(self):
        return self.name

