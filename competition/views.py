from django.shortcuts import render
from django.core.exceptions import ObjectDoesNotExist
from rest_framework.views import APIView, status
from rest_framework.response import Response

from .models import Competition, Article
from .serializers import CompetitionSerializer, CompetitionListSerializer, ArticleSerializer


class CompetitionView(APIView):
    def get(self, request, slug=None):
        if slug:
            try:
                competition = Competition.objects.prefetch_related(
                    'faqs', 'competition_videos', 'competition_images', 'competition_winners').get(slug=slug)
            except ObjectDoesNotExist:
                return Response('No competition with this slug.', status=status.HTTP_404_NOT_FOUND)

            serializer = CompetitionSerializer(competition)

        else:
            competitions = Competition.objects.all()

            serializer = CompetitionListSerializer(competitions, many=True)

        return Response(serializer.data)


class ArticleView(APIView):
    def get(self, request, slug=None):
        if slug:
            try:
                article = Article.objects.prefetch_related(
                    'article_images').get(slug=slug)
            except ObjectDoesNotExist:
                return Response('No article with this slug.', status=status.HTTP_404_NOT_FOUND)

            serializer = ArticleSerializer(article)

        else:
            article = Article.objects.prefetch_related(
                'article_images').all()

            serializer = ArticleSerializer(article, many=True)

        return Response(serializer.data)
