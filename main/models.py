from django.db import models

# Create your models here.


class ForumPost(models.Model):
    user = models.CharField(max_length=100)
    title = models.TextField(null=True, blank=True)
    post = models.TextField(null=True, blank=True)
    posted_at = models.DateTimeField(auto_now_add=True)
    up_vote = models.IntegerField(default=0)
    down_vote = models.IntegerField(default=0)

    def __str__(self):
        return str(self.user)+' : '+str(self.title)


class ForumPostReply(models.Model):
    forum_post = models.ForeignKey(ForumPost, on_delete=models.CASCADE)
    user = models.CharField(max_length=100)
    post = models.TextField()
    posted_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.user) + ' replying to : ' + str(self.post)




