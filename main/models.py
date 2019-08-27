from django.db import models

# Create your models here.


class ForumPost(models.Model):
    sender = models.CharField(max_length=100, primary_key=False)
    title = models.TextField()
    post = models.TextField()
    posted_at = models.DateTimeField(auto_now_add=True)
    up_vote = models.IntegerField(default=0)
    down_vote = models.IntegerField(default=0)

    def __str__(self):
        return str(self.sender)+' : '+str(self.title)


class ForumPostReply(models.Model):
    forum_post = models.ForeignKey(ForumPost, on_delete=models.CASCADE)
    user = models.CharField(max_length=100)
    post = models.TextField()
    posted_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.user)


class Contact(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField()
    message = models.TextField()

    sent_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name





