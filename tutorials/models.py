from django.db import models


# video tutorials


class Series(models.Model):
    SERIES_TYPES = (('VIDEO', 'Video'), ('TEXT', 'Text'), ('BOTH', 'Video and Text Combined'))

    title = models.CharField(max_length=100)
    description = models.TextField(blank=True, null=True)
    tutor = models.CharField(max_length=100, blank=True, null=True)
    price = models.PositiveIntegerField(default=1999)
    subscribed_users = models.TextField(null=True, blank=True, editable=True)
    number_of_tuts = models.PositiveSmallIntegerField(null=True, blank=True)
    template = models.ImageField(null=True, blank=True, upload_to='content/media/images/template_images/')
    template_link = models.URLField(null=True, blank=True)
    type = models.CharField(max_length=100, choices=SERIES_TYPES)

    def __str__(self):
        return self.title


class VideoTutorial(models.Model):
    series = models.ForeignKey(Series, on_delete=models.CASCADE)
    tut_id = models.PositiveSmallIntegerField(verbose_name='tutorial number', auto_created=True)
    title = models.CharField(max_length=200)
    description = models.TextField(blank=True, null=True)
    video = models.FileField(null=True, blank=True, upload_to='content/media/video_tutorials/')
    video_link = models.URLField(null=True, blank=True)

    def __str__(self):
        return self.title

    class Meta:
        unique_together = ('series', 'tut_id')


# text tutorials


class TextTutorial(models.Model):
    series = models.ForeignKey(Series, on_delete=models.CASCADE)
    tut_id = models.PositiveSmallIntegerField(verbose_name='tutorial number', auto_created=True)
    title = models.CharField(max_length=200)
    description = models.TextField(blank=True, null=True)
    lesson = models.TextField(verbose_name='Complete lesson : use html tags in here')

    def __str__(self):
        return str(self.tut_id) + ' : ' + str(self.title)

    class Meta:
        unique_together = ('series', 'tut_id')



