from rest_framework import generics
from quiz_app.paginations import MyPagination
from .models import Category, Question, Quiz
from .serializers import CategorySerializer, QuestionSerializer, QuizSerializer
from rest_framework.permissions import IsAuthenticated, AllowAny
# from rest_framework.authentication import TokenAuthentication, SessionAuthentication

# Create your views here.


class CategoryList(generics.ListAPIView):
    serializer_class = CategorySerializer
    queryset = Category.objects.all()
    permission_classes = [AllowAny]


class QuizList(generics.ListAPIView):
    serializer_class = QuizSerializer
    permission_classes = [AllowAny]

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
    # (Specific Pagination => only for this view)
    pagination_class = MyPagination
    permission_classes = [IsAuthenticated]
    
    # Multiple Authentication - respectively
    # authentication_classes = [TokenAuthentication, SessionAuthentication]

    def get_queryset(self):
        queryset = Question.objects.all()
        title = self.kwargs['title']
        queryset = queryset.filter(quiz__title=title)
        return queryset
