from django.contrib import admin
from .models.video import Category, Tag, Source, Video

# Register your models here.

admin.site.register(Category)
admin.site.register(Tag)
admin.site.register(Source)
admin.site.register(Video)
