from django.db import models
from django.utils import timezone

# Create your models here.

group_choices = (
        ('kajotters', 'Kajotters'),
        ('noenies', 'Noenies'),
        ('lippies', 'Lippies'),
        ('jeties', 'Jeties'),
        ('rabbits', 'Rabbits'),
        ('deltas', 'Deltas')
    )

class Maandprogramma(models.Model):
    author = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    group = models.CharField(
        max_length=50,
        choices=group_choices,
        default='kajotters'
    )
    text = models.TextField()
    created_date = models.DateTimeField(
            default=timezone.now)

    def __str__(self):
        return self.title

