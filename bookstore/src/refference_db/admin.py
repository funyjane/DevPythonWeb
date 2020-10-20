from django.contrib import admin
from . import models


admin.site.register(models.Author)
admin.site.register(models.Series)
admin.site.register(models.Genre)
admin.site.register(models.Publisher)
admin.site.register(models.Format)
admin.site.register(models.Age_res)
admin.site.register(models.Rating)