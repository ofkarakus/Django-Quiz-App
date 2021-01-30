from django.contrib import admin
from .models import Category, Quiz, Question, Answer
import nested_admin

# Register your models here.


class AnswerInline(nested_admin.NestedTabularInline):
    model = Answer
    extra = 2
    max_num = 4


class QuestionInline(nested_admin.NestedTabularInline):
    model = Question
    inlines = [AnswerInline]
    extra = 1
    max_num = 20


class QuizAdmin(nested_admin.NestedModelAdmin):
    model = Quiz
    inlines = [QuestionInline]


admin.site.register(Category)
admin.site.register(Quiz, QuizAdmin)
admin.site.register(Question)
admin.site.register(Answer)
