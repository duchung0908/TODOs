from django.db import models
from django import forms
from django.db import models
from django.contrib.auth.models import User
from model_utils.models import SoftDeletableModel, TimeStampedModel
import uuid


class Todo(TimeStampedModel, SoftDeletableModel):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    title = models.CharField(max_length=100)
    description = models.TextField(max_length=300, null=True, blank=True)
    completed = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True, editable=False)
    user_id = models.ForeignKey(User, related_name="todos", on_delete=models.CASCADE)

    class Meta:
        indexes = [
            models.Index(fields=["title"]),
        ]
        
        verbose_name = "Todo"
        verbose_name_plural = "Todos"

    def __str__(self):
        return self.title