from django.db import models

# Create your models here.

class Quiz(models.Model):
    qno = models.IntegerField(primary_key=True)
    question = models.CharField(max_length=300)
    ans = models.CharField(max_length=1)
    opt1 = models.CharField(max_length=35)
    opt2 = models.CharField(max_length=35)
    opt3 = models.CharField(max_length=35)
    opt4 = models.CharField(max_length=35)

    class Meta:
        managed = False
        db_table = 'quiz'

class Trial(models.Model):
    qno = models.IntegerField(primary_key=True)
    question = models.CharField(max_length=300)
    ans = models.CharField(max_length=1)
    opt1 = models.CharField(max_length=35)
    opt2 = models.CharField(max_length=35)
    opt3 = models.CharField(max_length=35)
    opt4 = models.CharField(max_length=35)

    class Meta:
        managed = False
        db_table = 'trial'
