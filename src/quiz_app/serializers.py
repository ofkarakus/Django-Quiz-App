from rest_framework import serializers
from .models import Category, Quiz


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = (
            'id',
            'name',
            'quiz_count'
        )


class QuizSerializer(serializers.ModelSerializer):
    class Meta:
        model = Quiz
        fields = (
            'title',
            'question_count'
        )
