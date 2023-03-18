from django.contrib import admin
from .models import Emotion

# Register your models here.
class EmotionAdmin(admin.ModelAdmin):
    list_display = ['subtype', 'type']
    list_filter = ['type']

admin.site.register(Emotion, EmotionAdmin)