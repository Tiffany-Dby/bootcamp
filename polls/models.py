from django.db import models

# Create your models here.
# Héritage en python Class(ClassParent)
class Question(models.Model):
  question_text = models.CharField(max_length=200)
  pub_date = models.DateField(auto_now_add=True)

class Choice(models.Model):
  question = models.ForeignKey(Question, on_delete=models.CASCADE, related_name="choices")
  choice_text = models.CharField(max_length=200)
  votes = models.IntegerField(default=0)