from django.db import models
from django.contrib.auth import get_user_model
from django.urls import reverse
from django.utils import timezone
from datetime import datetime
# Create your models here.

class Folder(models.Model):
    class Meta:
        constraints = [
            models.UniqueConstraint(fields=['title', 'user_owner'], name='unique_folder')
            ]
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=100)
    description = models.CharField(max_length=512, blank=True)
    last_access = models.DateTimeField(default=datetime.now)
    user_owner = models.ForeignKey(
                        get_user_model(),
                        on_delete=models.CASCADE,
                                   )
    def __str__(self):
        return self.title
    
    def get_absolute_url(self):
        return reverse('folder_detail', args=[str(self.id)])   


class Document(models.Model):
    class Meta:
        constraints = [
            models.UniqueConstraint(fields=['title', 'folder_parent'], name='unique_doc')
            ]
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=100)
    body = models.TextField(blank=True)
    last_access = models.DateTimeField(default=datetime.now)
    
    folder_parent = models.ForeignKey(
        Folder,
        on_delete=models.CASCADE,
    )


    def __str__(self):
        return self.title
    
    def get_absolute_url(self):
        return reverse('doc_detail', args=[str(self.id)])                       

