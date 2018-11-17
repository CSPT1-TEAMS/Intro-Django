from uuid import uuid4

from django.db import models
from django.contrib.auth.models import User


class Note(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid4, editable=False)
    author = models.CharField(max_length=25)
    title = models.CharField(max_length=150)
    body = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    last_modified = models.DateTimeField(auto_now=True)


class PersonalNote(Note):
    user = models.ForeignKey(User, blank=True, null=True, on_delete=models.CASCADE)