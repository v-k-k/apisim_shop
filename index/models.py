from django.db import models
from django.contrib.auth.models import User


class Subscriber(models.Model):
    #user = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True, default=None)
    name = models.CharField(max_length=64)
    email = models.EmailField()
    mobile = models.CharField(max_length=15)
    message = models.TextField(blank=True, null=True, default=None)
    ip = models.CharField(max_length=64, blank=True, null=True, default=None)
    mac = models.CharField(max_length=64, blank=True, null=True, default=None)

    def __str__(self):
        return 'Подписчик %s %s' % (self.name, self.email)
