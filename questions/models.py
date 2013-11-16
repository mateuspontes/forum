from django.db import models

class Question(models.Model):
  author = models.CharField(max_length = 80)
  title = models.CharField(max_length = 250)
  body = models.TextField()
  timestamp = models.DateTimeField()

  def __unicode__(self):
    return self.title
