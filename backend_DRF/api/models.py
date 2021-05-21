from django.db import models


class AgileValues(models.Model):
    title = models.CharField(max_length=30, blank=False)


class AgilePrinciples(models.Model):
    description = models.TextField(max_length=100, blank=False)
