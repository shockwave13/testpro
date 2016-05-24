from django.contrib import admin
from django.db import models
from .models import Section, Test, Question, Answer
# Register your models here.

class SectionAdmin(admin.ModelAdmin):
    model = Section
    prepopulated_fields = {"section_alias": ("section_name",)}

class TestAdmin(admin.ModelAdmin):
    model = Test
    list_filter = ['test_section_id']
    prepopulated_fields = {"test_alias": ("test_name",)}

class QuestionInLine (admin.StackedInline):
    model = Answer
    extra = 2

class QuestionAdmin(admin.ModelAdmin):
    model = Question
    list_filter = ['question_parretn_test_id']
    prepopulated_fields = {"question_alias": ("question_text",)}
    inlines = [QuestionInLine]

class AnswerAdmin(admin.ModelAdmin):
    model = Answer
    list_filter = ['answer_parretn_question_id']

admin.site.register(Section, SectionAdmin)
admin.site.register(Test, TestAdmin)
admin.site.register(Question, QuestionAdmin)
admin.site.register(Answer,AnswerAdmin)