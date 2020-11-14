from django.db import models
from refference_db.models import *
from book.models import *


class Filter(models.Model):
    genres = models.ManyToManyField(
        Genre, 
        verbose_name=("Genres")
        )

def __str__(self):
        return self.genres