from django.contrib import admin

# Register your models here.
from .models import Choice, Question

class QuestionAdmin(admin.ModelAdmin):
    fieldsets = [
        (None,              {'fields': ['question_text']}),
        ('Date information', {'fields': ['pub_date']}),
    ]

class ChoiceAdmin(admin.ModelAdmin):
    fields = ['choice_text', 'question']

admin.site.register(Question, QuestionAdmin)
admin.site.register(Choice, ChoiceAdmin)
