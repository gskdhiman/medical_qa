from django.db import models


class QuestionAnswer(models.Model):
    # id = models.IntegerField(max_length=10, unique=True,auto_now_add=True)
    question = models.CharField(max_length=100)
    context = models.CharField(max_length=100)
    answer = models.CharField(max_length=100)

    def __str__(self):
        return self.answer