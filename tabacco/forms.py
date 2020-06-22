from django import forms
from .models import ReviewsTabacco

class ReviewTabaccoForm(forms.ModelForm):

    class Meta:
        model = ReviewsTabacco
        fields = ['name', 'text']