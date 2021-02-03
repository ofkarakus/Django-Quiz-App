from django.urls import path
from quiz_app.views import CategoryList, QuestionList, QuizList


urlpatterns = [
    path('category/', CategoryList.as_view(), name='categories'),
    path('category/<category>/', QuizList.as_view(), name='quizzes'),
    path('title/<title>/', QuestionList.as_view(), name='questions'),
]
