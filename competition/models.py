from django.db import models


class Article(models.Model):
    title = models.CharField(max_length=255)
    slug = models.SlugField(blank=True, null=True)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class Competition(models.Model):
    title = models.CharField(max_length=255)
    slug = models.SlugField(blank=True, null=True)
    theme_color = models.CharField(max_length=30, blank=True, null=True)
    year = models.IntegerField()
    competition_logo = models.ImageField(upload_to='competitions/logo/')
    cover_image = models.ImageField(upload_to='competitions/covers/')
    competition_report = models.FileField(
        upload_to='competitions/competition_report/')
    detail_title = models.CharField(max_length=200)
    detail_content = models.TextField()
    content_image = models.ImageField(upload_to='competitions/detail/')
    scoreboard = models.FileField(upload_to='competitions/scoreboard/')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title


class CompetitionWinningTeam(models.Model):
    competition = models.ForeignKey(
        Competition, on_delete=models.CASCADE, related_name='competition_winners')
    position = models.IntegerField()
    team_name = models.CharField(max_length=255)
    image = models.ImageField(upload_to='competitions/winners/')

    class Meta:
        unique_together = ('competition', 'position')

    def __str__(self):
        return f'{self.competition}: {self.team_name} - {self.position}'


class MediaImage(models.Model):
    image = models.ImageField(upload_to='images/')
    tag = models.CharField(max_length=20, choices=[
        ('gallery', 'Gallery'),
        ('sponsor', 'Sponsor'),
        ('main_prize_laptop', 'Main_Prize_Laptop'),
        ('main_prize_phone', 'Main_Prize_Phone'),
        ('other_prize', 'Other_Prize'),
        ('general', 'General'),
    ])
    competition = models.ForeignKey(
        Competition, null=True, blank=True, on_delete=models.CASCADE, related_name='competition_images')
    article = models.ForeignKey(
        Article, null=True, blank=True, on_delete=models.CASCADE, related_name='article_images')


class MediaVideo(models.Model):
    video_file = models.FileField(upload_to='videos/')
    competition = models.ForeignKey(
        Competition, null=True, blank=True, on_delete=models.CASCADE, related_name='competition_videos')
    article = models.ForeignKey(
        Article, null=True, blank=True, on_delete=models.CASCADE, related_name='article_videos')


class FAQ(models.Model):
    question = models.CharField(max_length=300)
    answer = models.TextField()
    competition = models.ForeignKey(
        Competition, related_name='faqs', on_delete=models.SET_NULL, blank=True, null=True)
