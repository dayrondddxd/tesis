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








class MoodleQuizAttempt(models.Model):
    id = models.BigIntegerField(primary_key=True)
    quiz = models.BigIntegerField()  # ID del cuestionario en Moodle (mdl_quiz)
    userid = models.BigIntegerField()  # ID del usuario en Moodle (mdl_user)
    state = models.CharField(max_length=100)
    timestart = models.BigIntegerField()
    timefinish = models.BigIntegerField()
    sumgrades = models.FloatField()  # Calificación obtenida

    class Meta:
        db_table = 'mdl_quiz_attempts'
        managed = False












      