from django import forms
from . import models


class CreateGenreForm(forms.ModelForm):
    class Meta:
        model = models.Genre
        fields = (
            'genre',
            'description'
        )

class UpdateGenreForm(forms.ModelForm):
    class Meta:
        model = models.Genre
        fields = (
            'genre',
            'description'
        )

class CreateAuthorForm(forms.ModelForm):
    class Meta:
        model = models.Author
        fields = (
            'author',
            'biography'
        )

class UpdateAuthorForm(forms.ModelForm):
    class Meta:
        model = models.Author
        fields = (
            'author',
            'biography'
        )

class CreateSeriesForm(forms.ModelForm):
    class Meta:
        model = models.Series
        fields = (
            'title',
            'description'
        )

class UpdateSeriesForm(forms.ModelForm):
    class Meta:
        model = models.Series
        fields = (
            'title',
            'description'
        )

class CreatePublisherForm(forms.ModelForm):
    class Meta:
        model = models.Publisher
        fields = (
            'house',
            'history'
        )

class UpdatePublisherForm(forms.ModelForm):
    class Meta:
        model = models.Publisher
        fields = (
            'house',
            'history'
        )

class CreateFormatForm(forms.ModelForm):
    class Meta:
        model = models.Format
        fields = ('format',)

class UpdateFormatForm(forms.ModelForm):
    class Meta:
        model = models.Format
        fields = ('format',)

class CreateAgeresForm(forms.ModelForm):
    class Meta:
        model = models.Age_res
        fields = ('age_res',)

class UpdateAgeresForm(forms.ModelForm):
    class Meta:
        model = models.Age_res
        fields = ('age_res',)

class CreateRatingForm(forms.ModelForm):
    class Meta:
        model = models.Rating
        fields = ('rating',)

class UpdateRatingForm(forms.ModelForm):
    class Meta:
        model = models.Rating
        fields = ('rating',)