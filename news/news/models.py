from django.db import models
from django.urls import reverse

# Create your models here.
class News(models.Model):
    titel_text = models.CharField(max_length=200)
    text_news=models.TextField()
    pub_date = models.DateTimeField(auto_now_add=True)
    
    def get_absolute_url(self):
        return reverse('concretnews', args=[self.id])
