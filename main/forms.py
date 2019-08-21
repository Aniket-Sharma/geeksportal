from django import forms
from .models import ForumPostReply, ForumPost


class ForumPostForm(forms.ModelForm):

    class Meta:
        model = ForumPost
        fields = ('title', 'post',)

        widgets = {
            'title': forms.Textarea(attrs={'placeholder': 'Title of your post'}),
            'post': forms.Textarea(attrs={'placeholder': 'Write your post (use html tags for effects)'})
        }


class ForumReplyForm(forms.ModelForm):

    class Meta:
        model = ForumPostReply
        fields = ('post',)

        widgets = {
            'post': forms.Textarea(attrs={'placeholder': 'Write a Reply'})
        }

