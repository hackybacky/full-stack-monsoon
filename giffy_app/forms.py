from django import forms

from .models import Image


# We use Django's built-in ModelForm class
class UploadImageForm(forms.ModelForm):
  class Meta:
    model = Image

    fields = ["image", "title" , "description"]

    widgets = {
      "title": forms.Textarea(
        attrs={
          "cols": 60,
          "rows": 3,
        }
      ),
      "description": forms.Textarea(
        attrs={
          "cols": 60,
          "rows": 3,
        }
      ),
    }