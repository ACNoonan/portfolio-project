from django.db import models


class Blog(models.Model):
    title = models.CharField(max_length=200)
    image = models.ImageField(upload_to='images/')
    post = models.TextField()
    pubdate = models.DateTimeField()

    def __str__(self):
        return self.title

    def summary(self):
        return self.post[:100]

    def pubdate_pretty(self):
        return self.pubdate.strftime('%B %e, %Y')