from django.db import models

class NewsArticle(models.Model):
    id = models.AutoField(primary_key=True)
    end_year = models.CharField(max_length=255, null=True, blank=True)
    intensity = models.CharField(max_length=255)
    sector = models.CharField(max_length=255)
    topic = models.CharField(max_length=255)
    insight = models.CharField(max_length=255)
    url = models.CharField(max_length=512)
    region = models.CharField(max_length=255, blank=True)
    start_year = models.CharField(max_length=255)
    impact = models.CharField(max_length=255, blank=True)
    added = models.CharField(max_length=255)
    published = models.CharField(max_length=255)
    country = models.CharField(max_length=255, blank=True)
    relevance = models.CharField(max_length=255)
    pestle = models.CharField(max_length=255)
    source = models.CharField(max_length=255)
    title = models.CharField(max_length=512)
    likelihood = models.CharField(max_length=255)

    class Meta:
        db_table="tblnewsdata"

