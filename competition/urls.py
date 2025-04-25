from django.urls import path

from .views import CompetitionView

urlpatterns = [
    path('previous-competition/<slug:slug>/',
         CompetitionView.as_view(), name='competition'),
    path('previous-competition/', CompetitionView.as_view(), name='competitions')
]
