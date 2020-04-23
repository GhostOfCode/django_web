import datetime
from django.db import models
from django.utils import timezone


class Article(models.Model):
    article_title = models.CharField('Article Title', max_length=100)
    article_text = models.TextField('Article text')
    pub_date = models.DateTimeField('Publication date')

    def __str__(self):
        return self.article_title

    def was_publised_recently(self):
        return self.pub_date >= (timezone.now() - datetime.timedelta(days=3))


class Comment(models.Model):
    article = models.ForeignKey(Article, on_delete=models.CASCADE)
    comment_author = models.CharField('Comments author', max_length=75)
    comment_text = models.CharField('Text of comment', max_length=200)

    def __str__(self):
        return self.comment_author
