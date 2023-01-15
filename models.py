from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse

# Create your models here.
class Quiz(models.Model):
    title = models.CharField(max_length=200,null=True)
    
class Question(models.Model):
    Quiz = models.ForeignKey(Quiz, on_delete=models.CASCADE)
    question = models.CharField(max_length=200,null=True)
    op1 = models.CharField(max_length=200,null=True)
    op2 = models.CharField(max_length=200,null=True)
    op3 = models.CharField(max_length=200,null=True)
    op4 = models.CharField(max_length=200,null=True)
    ans = models.CharField(max_length=200,null=True)
    
    def __str__(self):
        return self.question

    def get_absolute_url(self):
        return reverse('quiz-detail', kwargs={'pk': self.pk})