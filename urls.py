from django.urls import path
from .views import (
    QuizListView,
    QuizDetailView,
    QuizCreateView,
    QuizUpdateView,
    QuizDeleteView
)
from . import views

urlpatterns = [
    path('', QuizListView.as_view(), name='quiz-home'),
    path('quiz/<int:pk>/', QuizDetailView.as_view(), name='quiz-detail'),
    path('quiz/new/', QuizCreateView.as_view(), name='quiz-create'),
    path('quiz/<int:pk>/update/', QuizUpdateView.as_view(), name='quiz-update'),
    path('quiz/<int:pk>/delete/', QuizDeleteView.as_view(), name='quiz-delete'),
    path('about/', views.about, name='quiz-about'),
]