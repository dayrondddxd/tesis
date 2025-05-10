from django.db import models

# Create your models here.
class Integration(models.Model):
    userid = models.AutoField(primary_key=True)
    username = models.CharField(max_length=50)
    password = models.CharField(max_length=50)
    firstname = models.CharField(max_length=50)
    lastname = models.CharField(max_length=50)
    email = models.CharField(max_length=50)
    roleid = models.IntegerField()





# from django.db import models
# from django.contrib.auth.models import User

# class UserProfile(models.Model):
#     user = models.OneToOneField(User, on_delete=models.CASCADE)
#     moodle_id = models.IntegerField(unique=True)
#     completed_courses = models.JSONField(default=list)  # Almacena IDs de cursos
    
#     def __str__(self):
#         return f"{self.user.username} - Moodle ID: {self.moodle_id}"














      