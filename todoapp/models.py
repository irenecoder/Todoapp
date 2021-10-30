from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Topic(models.Model):
    text = models.CharField(max_length=200)
    date_added = models.DateTimeField(auto_now=True)
    owner = models.ForeignKey(User,on_delete=models.CASCADE)
    def __str__(self):
        #return a string
        return self.text

class Entry(models.Model):

    """something specific learnt about a topic"""
    topic = models.ForeignKey(Topic,on_delete=models.CASCADE)
    text = models.TextField()
    date_added = models.DateTimeField(auto_now=True)


    class Meta:
        verbose_name_plural = 'entries'

        def __str__(self):

            #return string representation of the model
            return self.text[:50] + "..." 
 
