from django import forms
from .models import ReviewsHookah

class ReviewHookahForm(forms.ModelForm):

    class Meta:
        model = ReviewsHookah
        fields = ['name', 'text']
