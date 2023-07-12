from django.conf import settings
from django.db import models

class Image(models.Model):
  # image title, not blank string with maximum of 60 characters
  title = models.CharField(max_length=60, blank=False)
  image = models.ImageField(max_length=36)
  description = models.CharField(max_length=1000 , blank= True)
  # image upload date and time
  uploaded_date = models.DateTimeField()

  # link to the user that uploaded the image
  uploaded_by = models.ForeignKey(
    settings.AUTH_USER_MODEL,
    on_delete=models.CASCADE,
  )

  def __str__(self) -> str:
    return f"Image<{self.id}>"