from django.db import models

class Author(models.Model):
    author = models.CharField(
        "Author",
        max_length=50,
        blank=False,
        null=False
    )

    biography = models.TextField(
        "About author",
        max_length=500,
        blank=True,
        null=True
    )

    def __str__(self):
        return self.author


class Series(models.Model):
    title = models.CharField(
        "Series title",
        max_length=100,
        blank=False,
        null=False
    )

    description = models.TextField(
        "About the series",
        max_length=500,
        blank=True,
        null=True
    )

    def __str__(self):
        return self.title


class Genre(models.Model):
    genre = models.CharField(
        "Genre",
        max_length=50,
        blank=False,
        null=False
    )

    description = models.TextField(
        "About this genre",
        max_length=500,
        blank=True,
        null=True
    )

    def __str__(self):
        return self.genre


class Publisher(models.Model):
    house = models.CharField(
        "Publisher",
        max_length=50,
        blank=False,
        null=False

    )

    history = models.TextField(
        "More from this publisher",
        max_length=500,
        blank=True,
        null=True
    )

    def __str__(self):
        return self.house


class Format(models.Model):
    format = models.CharField(
        "Format",
        max_length=50,
        blank=False,
        null=False
    )

    def __str__(self):
        return self.format


class Age_res(models.Model):
    format = models.CharField(
        "Age restrictions",
        max_length=50,
        blank=False,
        null=False
    )

    def __str__(self):
        return self.author


class Rating(models.Model):
    format = models.CharField(
        "Rating",
        max_length=50,
        blank=False,
        null=False
    )

    def __str__(self):
        return self.author
