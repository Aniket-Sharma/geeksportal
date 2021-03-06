from django.urls import path
from .views import IndexPageView, SeriesContentView


urlpatterns = [
    path('', IndexPageView.as_view(), name='tut_index'),
    path('tut/<int:series_pk>', SeriesContentView.as_view(), name='series_content'),
]
