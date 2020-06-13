from django.db import models

# my models here.
class todo(models.Model):
    content = models.TextField()