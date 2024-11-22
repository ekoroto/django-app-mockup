from django.db import models


class Instance(models.Model):
    name = models.CharField(max_length=255, primary_key=True)
    data = models.JSONField()
