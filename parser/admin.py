from django.contrib import admin
from parser import models

# Register your models here.
admin.site.register(models.TelegramLogin)
admin.site.register(models.Category)
admin.site.register(models.News)
