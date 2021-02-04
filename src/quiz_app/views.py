from rest_framework import generics

from quiz_app.paginations import MyPagination
from .models import Category, Question, Quiz
from .serializers import CategorySerializer, QuestionSerializer, QuizSerializer

# Create your views here.


class CategoryList(generics.ListAPIView):
    serializer_class = CategorySerializer
    queryset = Category.objects.all()


class QuizList(generics.ListAPIView):
    serializer_class = QuizSerializer

    # overwrite queryset with get_queryset() method
    def get_queryset(self):
        queryset = Quiz.objects.all()
        category = self.kwargs['category']  # backend, frontend

        # ACCESSING PARENT MODEL'S PROPERTIES FROM CHILD MODEL
        # ! => (starts with lowercase initial letter)
        # <modelName>__<propName>  ==> category__id
        queryset = queryset.filter(category__name=category)
        return queryset


class QuestionList(generics.ListAPIView):
    serializer_class = QuestionSerializer
    pagination_class = MyPagination  # (Specific Pagination => only for this view)

    def get_queryset(self):
        queryset = Question.objects.all()
        title = self.kwargs['title']
        queryset = queryset.filter(quiz__title=title)
        return queryset
