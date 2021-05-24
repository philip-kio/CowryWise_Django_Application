from django.db import models
import uuid

# Create your models here.
class TimeUUID(models.Model):
    text = models.CharField(max_length=2)
    time_date = models.DateTimeField(auto_now_add=True)
    uuid_value = models.UUIDField(default=uuid.uuid4,unique=True,editable=False)


    def __str__(self):
        return self.text