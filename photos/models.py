from django.db import models

# Create your models here.
class Photo(models.Model):
    LICENSES = (
        ('RIG', 'COPYRIGHT'),
        ('LEF', 'COPYLEFT'),
        ('CC', 'CREATIVE COMMONS')
    )
    name = models.CharField(max_length=150)
    url = models.URLField()
    description = models.TextField(blank=True, null=True, default='')
    license = models.CharField(max_length=3, choices=LICENSES)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name