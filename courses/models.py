from django.db import models
from integration.models import Integration

# Create your models here.
class Course(models.Model):
    # moodle_id = models.IntegerField(null=True, blank=True)  # Para almacenar ID de Moodle
    courseid = models.AutoField(primary_key=True)
    fullname = models.CharField(max_length=50)
    shortname = models.CharField(max_length=50)
    categoryid = models.IntegerField()
    # qualification = models.BooleanField()
    # complete = models.BooleanField()


# class CourseUser(models.Model):
    # moodle_id = models.IntegerField(null=True, blank=True)  # Para almacenar ID de Moodle
    # courseid = models.ForeignKey(Course, on_delete=models.CASCADE)
    # userid = models.ForeignKey(Integration)
    # class asignaturas
    