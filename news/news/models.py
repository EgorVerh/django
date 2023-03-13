from django.db import models

# Create your models here.
class News(models.Model):
    titel_text = models.CharField(max_length=200)
    text_news=models.TextField()
    pub_date = models.DateTimeField(auto_now_add=True)
