from django import forms
from django.db.models import fields
from django.forms import ModelForm
from product.models import Review

class ReviewForm(forms.ModelForm):

    content=forms.CharField(label='REVIEW',widget=forms.Textarea)

    class Meta:
        model=Review
        fields=['content','rate']