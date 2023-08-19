from django import forms
from django.urls import reverse

from .models import *


class BookForm(forms.ModelForm):

    class Meta:
        model = Book
        exclude = "slug", "views"

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['author'].empty_label = "Not Chosen"
        attrs = self.fields['author'].widget.attrs
        attrs['btn_ref'] = reverse("add_author")

        self.fields['genre'].empty_label = "Not Chosen"
        attrs = self.fields['genre'].widget.attrs
        attrs['btn_ref'] = reverse("add_genre")
