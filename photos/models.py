from django.contrib.auth.models import User
from django.db import models
from .settings import LICENSES

# Create your models here.
class Photo(models.Model):
    VISIBILITY = (
        ('PUB', 'Público'),
        ('PRI', 'Privado')
    )
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=150)
    url = models.URLField()
    visibility = models.CharField(max_length=3, choices=VISIBILITY, default='PUB')
    description = models.TextField(blank=True, null=True, default='')
    license = models.CharField(max_length=3, choices=LICENSES)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name