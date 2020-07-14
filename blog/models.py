from django.db import models

# Create your models here.

class Blog(models.Model):
    title = models.CharField(max_length=200)
    pub_date = models.DateTimeField('data published')
    body = models.TextField()

    def __str__(self):
        return self.title

    def summary(self):
        return self.body[:100]
    
    def summary2(self):
        return self.pub_date[:9]
    