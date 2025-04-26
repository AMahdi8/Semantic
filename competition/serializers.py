from rest_framework import serializers

from .models import *


class MediaImageSerializer(serializers.ModelSerializer):

    class Meta:
        model = MediaImage
        fields = ['image', 'tag', 'competition', 'article']


class MediaVideoSerializer(serializers.ModelSerializer):

    class Meta:
        model = MediaVideo
        fields = ['video_file', 'competition']


class FAQSerializer(serializers.ModelSerializer):

    class Meta:
        model = FAQ
        fields = ['question', 'answer', 'competition']


class WinnersSerializer(serializers.ModelSerializer):

    class Meta:
        model = CompetitionWinningTeam
        fields = ['position', 'team_name', 'image', 'competition']


class CompetitionSerializer(serializers.ModelSerializer):
    competition_winners = WinnersSerializer(many=True)
    competition_images = MediaImageSerializer(many=True)
    competition_videos = MediaVideoSerializer(many=True)
    faqs = FAQSerializer(many=True)

    class Meta:
        model = Competition
        fields = ['title', 'slug', 'year', 'competition_logo', 'cover_image', 'competition_report', 'detail_title', 'detail_content',
                  'content_image', 'scoreboard', 'competition_images', 'competition_winners', 'competition_videos', 'faqs']


class CompetitionListSerializer(serializers.ModelSerializer):

    class Meta:
        model = Competition
        fields = ['title', 'slug', 'year', 'cover_image',
                  'competition_report', 'competition_logo']


class ArticleSerializer(serializers.ModelSerializer):
    article_images = MediaImageSerializer(many=True)
    article_viedos = MediaVideoSerializer(many=True)

    class Meta:
        model = Article
        fields = ['title', 'slug', 'content',
                  'article_images', 'article_videos', 'created_at']
