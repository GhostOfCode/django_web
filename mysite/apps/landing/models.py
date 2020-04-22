from django.db import models


class Subscriber(models.Model):
    email = models.EmailField()
    user_name = models.CharField(max_length=75)

    def __str__(self):
        return self.user_name
