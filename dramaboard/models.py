from django.db import models
from django.conf import settings
from imagekit.models import ImageSpecField
from imagekit.processors import ResizeToFill

# Create your models here.
class Drama(models.Model):
    title = models.CharField(max_length=50)
    content = models.TextField()
    score_Choices = (
        ('★','★'),
        ('★★','★★'),
        ('★★★','★★★'),
        ('★★★★','★★★★'),
        ('★★★★★','★★★★★'),
    )
    score = models.TextField(choices=score_Choices)
    writer = models.CharField(max_length=100)
    date = models.DateTimeField()
    img = models.ImageField(upload_to="drama/", blank = True, null = True)
    image_thumbnail = ImageSpecField(source = 'img', processors=[ResizeToFill(120,100)])
    like = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name="like", blank=True)

    def __str__(self):
          return self.title

    def summary(self):
        return self.content[:50]


class Meta:
    ordering = ['-created']