from django.db import models

# Create your models here.

#Creating Company Model

from django.db import models

class FAQ(models.Model):
    question = models.TextField()
    answer = models.TextField()
    keywords = models.JSONField(blank=True, null=True)  # JSON field for flexible metadata


    