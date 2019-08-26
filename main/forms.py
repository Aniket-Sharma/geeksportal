from django import forms
from .models import ForumPostReply, ForumPost, Contact


class ForumPostForm(forms.ModelForm):

    class Meta:
        model = ForumPost
        fields = ('title', 'post',)

        widgets = {
            'title': forms.Textarea(attrs={'placeholder': 'Title of your post', 'class': 'Title'}),
            'post': forms.Textarea(attrs={'placeholder': 'Write your post (use html tags for effects)'})
        }


class ForumReplyForm(forms.ModelForm):

    class Meta:
        model = ForumPostReply
        fields = ('post',)

        widgets = {
            'post': forms.Textarea(attrs={'placeholder': 'Write a Reply', 'class': 'Reply'})
        }


class ContactForm(forms.ModelForm):
    name = forms.CharField(widget=forms.TextInput(
        attrs={'placeholder': 'What should we call you ?'}))
    email = forms.EmailField(label='Email', widget=forms.TextInput(
        attrs={'placeholder': 'Where can we email you back ?'}))

    class Meta:
        model = Contact
        fields = '__all__'
        widgets = {
            'message': forms.Textarea(attrs={'placeholder': 'What\'s on your mind ?'})
        }

