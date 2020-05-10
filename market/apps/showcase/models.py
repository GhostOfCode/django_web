from django.db import models


class Subscriber(models.Model):
    user_name = models.CharField('Ваше имя', max_length=100)
    user_email = models.EmailField('Ваша почта')

    def __str__(self):
        return '{0} - {1}'.format(self.user_name, self.user_email)

    class Meta:
        verbose_name = 'Subscriber'
        # verbose_name_plural = 'A lot of users'
