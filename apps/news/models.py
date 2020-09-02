from django.db import models


class News(models.Model):
    news_id = models.AutoField(primary_key=True)
    user_id = models.CharField(max_length=48)
    title = models.CharField(max_length=200)
    content = models.TextField()
    time = models.DateTimeField()
    importance = models.IntegerField()
    defunct = models.CharField(max_length=1)

    class Meta:
        managed = False
        db_table = 'news'

