from django.urls import path
from . import views
from .views import PostList

urlpatterns = [
    path('', PostList.as_view()),
    path('post/<int:pk>/', views.post_detail, name='post_detail'),

]