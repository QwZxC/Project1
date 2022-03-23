import datetime

from django.db import models

class Arcticle(models.Model):
    arcticle_title = models.CharField('Название статьи', max_length= 150)
    arcticle_text = models.TextField('Текст статьи')
    pub_date = models.DateTimeField('Дата публикации')

    def __str__(self):
        return self.arcticle_title

    def was_published_recently(self):
        return self.pub_date >= (timezone.now() - datetime.timedelta(days = 7))

    class Meta:
        verbose_name = 'Кринж'
        verbose_name_plural ='КринжЫ'

class Comment(models.Model):
    arcticle = models.ForeignKey(Arcticle, on_delete= models.CASCADE)
    author_name = models.CharField('Имя автора', max_length= 50)
    comment_text = models.CharField('Текст комментария', max_length= 350)

    def __str__(self):
        return self.author_name
    class Meta:
        verbose_name = 'Кринж коммент'
        verbose_name_plural ='Кринж комменты '