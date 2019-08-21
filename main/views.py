from django.shortcuts import render
from django.views.generic import TemplateView
from .models import ForumPost, ForumPostReply
from .forms import ForumPostForm, ForumReplyForm


class IndexPageView(TemplateView):
    template_name = 'main/index.html'


class ChangeLanguageView(TemplateView):
    template_name = 'main/change_language.html'


class HomePageView(TemplateView):
    template_name = 'main/home.html'

    def get(self, request):

        post_form = ForumPostForm()
        reply_form = ForumReplyForm()

        posts = ForumPost.objects.all().order_by('-posted_at')
        replies = ForumPostReply.objects.all().order_by('-posted_at')

        args = {'posts': posts, 'replies': replies, 'post_form': post_form, 'reply_form': reply_form}

        return render(request, self.template_name, args)

