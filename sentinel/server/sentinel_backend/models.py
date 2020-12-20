from django.db import models

class content_input(models.Model):
    content = models.CharField(max_length = 1000)
