from django.db import models

# Create your models here.
class Book(models.Model):
    title = models.CharField(max_length=200)
    subtitle = models.CharField(max_length=250)
    content = models.TextField()
    author = models.CharField(max_length=128)
    isbn = models.CharField(max_length=20)
    price = models.DecimalField(max_digits=50 , decimal_places=2)

    def __str__(self):
        return self.title
