from django.contrib import admin

from .models import Question, Choice, Anwser

class ChoiceInline(admin.StackedInline):
    model = Choice
    extra = 1
class QuestionAdmin(admin.ModelAdmin):
    fieldsets = [
        (None, {"fields": ['question_text']}),
        ('Date Information', {'fields': ['pub_date']}),
    ]
    inlines = [ChoiceInline]

class ChoiceAdmin(admin.ModelAdmin):
    fields = ['choice_text', 'votes']

admin.site.register(Question, QuestionAdmin)
admin.site.register(Choice, ChoiceAdmin)
admin.site.register(Anwser)