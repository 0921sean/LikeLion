from django import forms
from .models import Comment

class CommentForm(forms.ModelForm):
    comment = forms.CharField(widget=forms.Textarea(attrs={'rows':'1', 'placeholder':'댓글을 달아주세요.'}))
    class Meta:
        model = Comment
        fields = ['comment']