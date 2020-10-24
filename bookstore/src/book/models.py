from django.db import models
from refference_db.models import *
from datetime import date

class Book(models.Model):
    name = models.CharField(
        "Title",
        max_length=100,
        blank=False,
        null=False
    )

    cover_photo = models.ImageField(
        "Cover",
        upload_to='media/'
    )

    author_id = models.ManyToManyField(Author)

    genre_id = models.ManyToManyField(Genre)

    series = models.ForeignKey(
        Series,
        default=1,
        on_delete=models.PROTECT
    )

    publisher = models.ForeignKey(
        Publisher,
        default=1,
        on_delete=models.PROTECT
    )

    price = models.DecimalField(
        "Price (BYN)",
        default=0.0,
        max_digits=10,
        decimal_places=2,
        blank=False,
        null=False
    )


    publishing_date = models.DateField(
        "Date published",
        default=date.today,
        blank=False,
        null=False
    )

    pages_num = models.PositiveIntegerField(
        "Number of pages",
        default=0,
        blank=False,
        null=False
    )

    binding = models.CharField(
        "Binding",
        default="",
        max_length=50,
        blank=False,
        null=False
    )
    
    format = models.ForeignKey(
        Format,
        default=1,
        on_delete=models.PROTECT
    )

    ISBN = models.PositiveIntegerField(
        "ISBN",
        max_length=13,
        default=0,
        blank=False,
        null=False
    )

    weight = models.PositiveIntegerField(
        "Weight (g)",
        default=0,
        blank=False,
        null=False
    )

    age_res = models.ForeignKey(
        Age_res,
        default=1,
        on_delete=models.PROTECT
    )

    stock_number = models.PositiveIntegerField(
        "Left in stock",
        default=0,
        blank=False,
        null=False
    )

    ACTIVE_OPTIONS = ((True, 'Yes'), (False, 'No'))

    is_active = models.BooleanField(
        "Is active?",
        choices=ACTIVE_OPTIONS,
        default=True,
        blank=False,
        null=False
    )

    rating = models.ForeignKey(
        Rating,
        default=1,
        on_delete=models.PROTECT
    )


    entry_date = models.DateTimeField(
        "Date of entry",
        auto_now_add=True,
        null=True,
        blank=True
    )

    update_date = models.DateTimeField(
        "Date of update",
        auto_now=True,
        null=True,
        blank=True
    )



    def __str__(self):
        return self.name