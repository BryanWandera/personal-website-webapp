from django.db import models

# Create your models here.
class PortfolioPiece(models.Model):
    title = models.CharField(max_length=30)
    image = models.ImageField(upload_to='media/static/assets/portfolio-images')
    link = models.URLField(max_length=200)

    def __str__(self):
        return self.title

class AboutCopy(models.Model):
    title = 'about_copy'
    paragraph_one = models.TextField()
    paragraph_two = models.TextField()

    def __str__(self):
        return self.title