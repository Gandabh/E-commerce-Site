from django import forms
from blog.models import Comment
from django.forms import ModelForm



class CommentForm(forms.ModelForm):

    comment= forms.CharField(required=True,label='COMMENTS',widget=forms.Textarea(attrs={'class': 'col-sm-12',}))


    class Meta:
            model = Comment
            fields = (
              
                'comment',
            )

