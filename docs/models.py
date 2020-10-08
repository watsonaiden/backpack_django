from django.db import models
from django.contrib.auth import get_user_model
from django.urls import reverse

# Create your models here.

class Folder(models.Model):
    class Meta:
        unique_together =('title', 'user_owner')
    title = models.CharField(max_length=100, primary_key=True)
    description = models.CharField(max_length=512)
    user_owner = models.ForeignKey(
                        get_user_model(),
                        on_delete=models.CASCADE,
                                   )
    def __str__(self):
        return self.title
    
    def get_absolute_url(self):
        return reverse('folder_detail', args=[str(self.title)])   


class Document(models.Model):
    class Meta:
        unique_together = ('id', 'folder_parent')
    title = models.CharField(max_length=100)
    body = models.TextField()
    folder_parent = models.ForeignKey(
        Folder,
        on_delete=models.CASCADE,
    )


    def __str__(self):
        return self.title
    
    def get_absolute_url(self):
        return reverse('doc_detail', args=[str(self.id)])                       

