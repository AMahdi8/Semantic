from django.urls import path

from .views import ArticleView, CompetitionView

urlpatterns = [
    path('previous-competition/<slug:slug>/',
         CompetitionView.as_view(), name='competition'),
    path('previous-competition/', CompetitionView.as_view(), name='competitions'),
    path('articles/<slug:slug>/', ArticleView.as_view(), name='article'),
    path('articles/', ArticleView.as_view(), name='articles'),
]
