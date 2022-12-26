from django.db import models
class TableA(models.Model):
    word = models.CharField(max_length=255)
    word_count = models.IntegerField()
    corpus = models.CharField(max_length=255)
    corpus_date = models.IntegerField()
# Create your models here.
