from django.urls import path
from quiz_app.views import CategoryList


urlpatterns = [
    path('', CategoryList.as_view(), name='categories')
]
