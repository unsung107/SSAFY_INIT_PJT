from django import forms
from .models import Movie, Review, Genre

class CommentForm(forms.ModelForm):

    class Meta:
        model = Review
        fields = ['content', 'score']