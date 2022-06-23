from django.db import models

# Create your models here.
class Club(models.Model):
    name = models.CharField(max_length=30)
    body = models.CharField(max_length=100)
    number = models.IntegerField(null=True)

class Comment(models.Model):
    comment = models.CharField(max_length=100)
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.comment