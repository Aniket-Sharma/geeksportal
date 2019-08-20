from django.contrib import admin

from .models import VideoTutorial, Series, TextTutorial

admin.site.register(VideoTutorial)
admin.site.register(TextTutorial)
admin.site.register(Series)
