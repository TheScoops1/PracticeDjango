from django.contrib import admin

from .models import Question, Choice, Anwser

admin.site.register(Question)
admin.site.register(Choice)
admin.site.register(Anwser)