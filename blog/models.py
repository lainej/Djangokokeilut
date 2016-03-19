from django.db import models

class Posts(models.Model):
    title =  models.CharField()
    body =  models.TextField()
    date = models.DateTimeField()
    
    def __str__(self):
        return self.title
