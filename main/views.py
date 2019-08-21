from django.shortcuts import render, HttpResponse, HttpResponseRedirect, redirect
from django.views.generic import TemplateView
from django.contrib import messages
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

    def post(self, request, post_id=None):

        if post_id:

            form = ForumReplyForm(request.POST).save(commit=False)

            form.user = request.user.username

            form.forum_post = ForumPost.objects.get(pk=post_id)

            form.save()

            messages.success(request, "Your reply has been successfully posted!")

            return redirect('home')

        else:

            form = ForumPostForm(request.POST).save(commit=False)

            form.sender = request.user.username

            form.save()

            messages.success(request, "Your content is now online!")

            return redirect('home')







#
    # def post_forum_post(self, request):
    #
    #     form = ForumPostForm(request.POST)
    #
    #     form.save(commit=False)
    #
    #     form.user = request.user.username
    #
    #     form.save()
    #
    #     messages.success(request, "The content is now online! ")
    #
    #     return HttpResponseRedirect('home')
    #
    # def reply_forum_post(self, request, post_id):
    #     form = ForumPostForm(request.POST)
    #
    #     if form.is_valid():
    #         form.save(commit=False)
    #
    #         form.user = request.user.username
    #
    #         form.forum_post = post_id
    #
    #         form.save()
    #
    #         messages.success(request, "Your reply has been successfully posted!")
    #
    #     return HttpResponseRedirect('home')





