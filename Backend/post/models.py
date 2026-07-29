
from django.db import models
import uuid
from account.models import User
from django.utils.timesince import timesince

# Create your models here.


class PostAttachment(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    image = models.ImageField(upload_to='post_attachments')
    created_by = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='post_attachments')
    



class Post(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    body = models.TextField(blank=True)


    attachments = models.ManyToManyField(
        PostAttachment, related_name='posts', blank=True)

    # likes
    # likes counts

    created_at = models.DateTimeField(auto_now_add=True)
    created_by = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='posts')


    class Meta:
        ordering = ['-created_at']

    def created_by_formatted(self):


        return timesince(self.created_at) + " ago"
          

    


