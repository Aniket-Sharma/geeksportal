from django.contrib import admin

# Register your models here.
from .models import ForumPostReply, ForumPost


admin.site.register(ForumPost)
admin.site.register(ForumPostReply)

