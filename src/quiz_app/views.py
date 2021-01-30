from django.shortcuts import render
from rest_framework import generics
from .models import Category, Quiz
from .serializers import CategorySerializer, QuizSerializer

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
