from django.contrib import admin
from .models import Category,New,Advert,Media,Comment

# Register your models here.

admin.site.register(Category)
admin.site.register(New)
admin.site.register(Advert)
admin.site.register(Media)
admin.site.register(Comment)
