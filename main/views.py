from django.shortcuts import render, HttpResponse, HttpResponseRedirect, redirect
from django.views.generic import TemplateView
from django.contrib import messages
from .models import ForumPost, ForumPostReply, Contact
from tutorials.models import Series
from .forms import ForumPostForm, ForumReplyForm, ContactForm


class IndexPageView(TemplateView):
    template_name = 'main/index.html'

    def get(self, request):
        form = ContactForm()
        args = {'form': form}
        return render(request, self.template_name, args)

    def post(self, request):
        form = ContactForm(request.POST)
        form.save()
        messages.success(request, "Your message was sent successfully !")
        return redirect('index')


class ChangeLanguageView(TemplateView):
    template_name = 'main/change_language.html'


class ProfileView(TemplateView):
    template_name = 'main/profile.html'

    def get(self, request):
        all_series = Series.objects.all()
        posts = ForumPost.objects.filter(sender=request.user.username)
        replies = ForumPostReply.objects.filter(user=request.user.username).order_by('-posted_at')
        notifications = ForumPostReply.objects.none()
        for key in posts:
            temp = ForumPostReply.objects.all().filter(forum_post=key).order_by('-posted_at').exclude(user=request.user)
            notifications = notifications | temp

        args = {'all_series': all_series, 'posts': posts, 'replies': replies, 'notifications': notifications}
        if request.user.is_superuser:
            msgs = Contact.objects.all().order_by('-sent_at')
            args['msgs'] = msgs

        return render(request, self.template_name, args)


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





