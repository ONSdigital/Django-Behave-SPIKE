from django.db import models

# Create your models here.
class HomePage(models.Model):
    title = models.CharField(max_length=200)
    hero_text = models.TextField()
    hero_button_text = models.CharField(max_length=100)

    def __str__(self):
        return self.title