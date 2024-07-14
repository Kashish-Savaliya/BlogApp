from django.db import models
from django.contrib.auth.models import User
from django.utils.timezone import now

# Create your models here.
class Post(models.Model):
    sno=models.AutoField(primary_key=True)
    title=models.CharField(max_length=255)
    author=models.CharField(max_length=14)
    slug=models.CharField(max_length=130)
    views=models.IntegerField(default=0)
    pub_date=models.DateTimeField(blank=True)
    content=models.TextField()

    def __str__(self):
        return self.title + " by " + self.author

class BlogComment(models.Model):
    sno = models.AutoField(primary_key=True)
    comment = models.TextField()
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    post = models.ForeignKey(Post,on_delete=models.CASCADE)       #When a user deletes a blog, we want to delete all the comments associated with the blog post.
                                                                  #Here, the deletion of the comments depends upon the deletion of the blog post.
                                                                  #So, when the reference object is deleted, then all the objects that have references to it will also be deleted.
    parent = models.ForeignKey('self',on_delete=models.CASCADE, null=True)    #field called parent in a Django model that establishes a relationship with the same model, allowing each instance of the model to have a parent (which is another instance of the same model).
                                                                            # The on_delete=models.CASCADE part ensures that if a parent is deleted, all related child instances will also be deleted, and null=True allows instances to have no parent (i.e., be at the top of the hierarchy).
    timestamp = models.DateTimeField(default=now)

    def __str__(self):
        return self.comment[0:13] + "..." + "by" + " " + self.user.username