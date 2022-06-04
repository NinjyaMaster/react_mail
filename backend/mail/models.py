from django.conf import settings
from django.db import models
from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType
from django.contrib.contenttypes.fields import GenericRelation


class Tag(models.Model):
    creator = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    value = models.TextField(max_length=100, unique=True)
    content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE)
    object_id = models.PositiveIntegerField()
    content_object = GenericForeignKey("content_type", "object_id")

    def __str__(self):
        return self.value


class Email(models.Model):
    #user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="emails")
    sender = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="emails_sent")
    recipients=models.ManyToManyField(settings.AUTH_USER_MODEL, related_name="emails_received")
    #sender = models.ForeignKey("User", on_delete=models.PROTECT)
    #recipients=models.ManyToManyField("User", on_delete=models.PROTECT)
    subject= models.CharField(max_length=255)
    body=models.TextField(blank=True)
    timestamp = models.DateTimeField(auto_now=True)
    read =models.BooleanField(default=False)
    archived = models.BooleanField(default=False)
    tags = GenericRelation(Tag)

    def __str__(self):
        return f"{self.sender} {self.subject}"


class UserProfile(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="profile")
    bio = models.TextField()

    def __str__(self):
        return f"{self.__class__.__name__} object for {self.user}"