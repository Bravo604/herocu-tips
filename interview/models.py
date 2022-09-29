from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator


class Category(models.Model):
    name = models.CharField(max_length=40)

    def __str__(self):
        return self.name


class QuestionAnswer(models.Model):
    text = models.TextField(max_length=255)
    short_answer = models.TextField(max_length=255)
    answer = models.TextField(null=True, blank=True)
    importance = models.IntegerField(
        default=1,
        validators=[
            MaxValueValidator(100),
            MinValueValidator(1)
        ]
     )
    category = models.ForeignKey(Category, on_delete=models.CASCADE)

    def __str__(self):
        return self.text

