from django.db import models

# Create your models here.
# Create your models here.

class Twitter(models.Model):
    tweet_id = models.CharField(max_length=120)
    text = models.TextField()

    def _str_(self):
        return self.tweet_id