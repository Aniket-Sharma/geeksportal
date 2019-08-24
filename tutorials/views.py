from django.shortcuts import render, redirect, HttpResponseRedirect, HttpResponse
from django.views.generic import TemplateView
from .models import TextTutorial, VideoTutorial, Series
from django.contrib import messages
# Create your views here.


class IndexPageView(TemplateView):
    template_name = 'tutorials/index.html'

    def get(self, request):
        all_series = Series.objects.all()
        args = {'all_series': all_series}
        return render(request, self.template_name, args)

    def post(self, request):
        series = Series.objects.get(pk=request.POST.get('series'))
        user = request.POST.get('username')
        series.subscribed_users = user + ' ' + series.subscribed_users
        series.save()
        messages.success(request, 'You are now registered for %s Tutoral Series' %str(series.title) )
        return redirect('tut_index')


class SeriesContentView(TemplateView):
    template_name = 'tutorials/series-content.html'

    def get(self, request, series_pk):
        text_tutorials = TextTutorial.objects.filter(series=series_pk).order_by('tut_id')
        video_tutorials = VideoTutorial.objects.filter(series=series_pk).order_by('tut_id')
        args = {'text_tutorials': text_tutorials, 'video_tutorials': video_tutorials}
        return render(request, self.template_name, args)

