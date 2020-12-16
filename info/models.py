from django.db import models

class Info(models.Model):
    name = models.CharField(max_length=200)
    sex = models.TextField(blank=True)
    age = models.TextField(blank=True)
    phone = models.CharField(max_length=200)
    village_name = models.TextField(blank=True)
    add_relation = models.TextField(blank=True)
    local_government = models.TextField(blank=True)
    state = models.TextField(blank=True)
    pvc_number = models.CharField(max_length=200)