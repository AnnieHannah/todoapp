from django.db import models


# Model for storing todo activities.
class TodoModel(models.Model):
    class IsCompleted(models.IntegerChoices):
        completed = 1, 'Completed'
        not_completed = 0, 'Not completed'

    todo = models.CharField(max_length=500)
    is_completed = models.IntegerField(choices=IsCompleted.choices, default=IsCompleted.not_completed)
    expiry = models.DateTimeField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.todo
