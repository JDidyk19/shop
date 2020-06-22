from django import forms
from .models import ReviewsCoal

class ReviewCoalForm(forms.ModelForm):

    class Meta:
        model = ReviewsCoal
        fields = ['name', 'text']