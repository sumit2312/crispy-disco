from django.contrib import admin
from .models import Question, Comment, Request
# Register your models here.

admin.site.register(Question)
admin.site.register(Comment)
admin.site.register(Request)