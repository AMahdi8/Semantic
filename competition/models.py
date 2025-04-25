from django.db import models


class Article(models.Model):
    title = models.CharField(max_length=255)
    content = models.TextField()
    images = models.ForeignKey(
        'MediaImage', null=True, blank=True, on_delete=models.SET_NULL)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class Competition(models.Model):
    title = models.CharField(max_length=255)
    year = models.IntegerField()
    cover_image = models.ImageField(upload_to='competitions/covers/')
    competition_report = models.FileField(
        upload_to='competitions/competition_report/')


class CompetitionDetail(models.Model):
    competition = models.ForeignKey(
        Competition, on_delete=models.CASCADE, related_name='competition_detail')
    title = models.CharField(max_length=200)
    content = models.TextField()
    image = models.ForeignKey('MediaImage', null=True,
                              blank=True, on_delete=models.SET_NULL)


class CompetitionWinningTeam(models.Model):
    competition = models.ForeignKey(
        Competition, on_delete=models.CASCADE, related_name='competition_winners')
    position = models.CharField(max_length=255)
    team_name = models.CharField(max_length=255)
    scoreboard = models.TextField()
    image = models.ForeignKey('MediaImage', on_delete=models.CASCADE)


class CompetitionPrize(models.Model):
    competition = models.ForeignKey(Competition, on_delete=models.CASCADE)
    image = models.ForeignKey('MediaImage', on_delete=models.CASCADE)
    description = models.TextField()


class CompetitionSponsor(models.Model):
    competition = models.ForeignKey(
        Competition, on_delete=models.CASCADE, related_name='competition_sponsers')
    image = models.ForeignKey('MediaImage', on_delete=models.CASCADE)


class MediaImage(models.Model):
    image = models.ImageField(upload_to='media/images/')
    title = models.CharField(max_length=200, blank=True)
    tag = models.CharField(max_length=10, choices=[
        ('gallery', 'Gallery'),
        ('sponsor', 'Sponsor'),
        ('winner', 'Winner'),
        ('article', 'Article'),
        ('prize', 'Prize'),
        ('general', 'General'),
    ])
    competition = models.ForeignKey(
        Competition, null=True, blank=True, on_delete=models.CASCADE, related_name='competition_images')


class MediaVideo(models.Model):
    title = models.CharField(max_length=200)
    video_file = models.FileField(upload_to='media/videos/')
    competition = models.ForeignKey(
        Competition, null=True, blank=True, on_delete=models.CASCADE, related_name='competition_videos')


class FAQ(models.Model):
    question = models.CharField(max_length=300)
    answer = models.TextField()
    competition = models.OneToOneField(
        Competition, related_name='FAQ', on_delete=models.SET_NULL, blank=True, null=True)


class ContactMessage(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    title = models.CharField(max_length=255)
    email = models.EmailField()
    message = models.TextField()
    is_accepted = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)


class TeamRegistration(models.Model):
    university_name = models.CharField(max_length=200)
    team_name = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)


class TeamMember(models.Model):
    team = models.ForeignKey(
        TeamRegistration, on_delete=models.CASCADE, related_name='members')
    is_leader = models.BooleanField()
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    phone_number = models.CharField(max_length=20)
    student_id = models.CharField(max_length=20)
    personal_id = models.CharField(max_length=20)
    gender = models.CharField(max_length=10, choices=(
        ('man', 'Man'),
        ('woman', 'Woman'),
    ))
    degree = models.CharField(max_length=10, choices=(
        ('master', 'Master'),
        ('bachelor', 'Bachelor'),
        ('PH.D', 'PH.D'),
    ))
    email = models.EmailField()
