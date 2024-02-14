from django.db import models


class Article(models.Model):
    title = models.CharField(max_length=100,blank=True),
    slug = models.SlugField(blank=True),
    body = models.TextField(blank=True),
    date = models.DateTimeField(blank=True,auto_now_add=True),
    # add in thumbnail later
    # add in author later

    def __str__(self):
        print("The value of title is", str(self.title))
        return str(self.title)
