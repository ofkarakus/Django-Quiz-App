from django.urls import path
from quiz_app.views import CategoryList, QuizList


urlpatterns = [
    path('', CategoryList.as_view(), name='categories'),
    path('<category>/', QuizList.as_view(), name='quizzes')
]
