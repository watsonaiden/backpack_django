from django.db import models
from django.utils import timezone
from django.contrib.auth import get_user_model
from django.urls import reverse
# Create your models here.


class Reminder(models.Model):
    title = models.CharField(max_length=100)
    description = models.CharField(max_length=512, blank=True)
    deadline = models.DateTimeField(null=True)

    user_owner = models.ForeignKey(
                        get_user_model(),
                        on_delete=models.CASCADE,
                            )
    def __str__(self):
        return self.title

    def days_to_complete(self):
        td = self.deadline - timezone.now()
        
        return td.days, td.seconds//3600

    
    def get_absolute_url(self):
        return reverse('reminder_detail', args=[str(self.pk)])


