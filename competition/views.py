from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response

from .models import *
from .serializers import CompetitionSerializer, CompetitionListSerializer


class CompetitionView(APIView):
    def get(self, request, slug=None):
        if slug:
            competition = Competition.objects.prefetch_related(
                'faqs', 'competition_videos', 'competition_images', 'competition_winners').get(slug=slug)

            serializer = CompetitionSerializer(competition)

        else:
            competitions = Competition.objects.all()

            serializer = CompetitionListSerializer(competitions, many=True)

        return Response(serializer.data)
