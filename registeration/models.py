from django.db import models

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
