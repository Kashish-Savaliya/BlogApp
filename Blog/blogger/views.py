from django.shortcuts import render, HttpResponse, redirect
from blogger.models import Post, BlogComment
from django.contrib import messages
from django.contrib.auth.models import User
from blogger.templatetags import extras


# Create your views here.
def blogHome(request):
    allPosts = Post.objects.all()
    context = {'allPosts': allPosts}
    # print(context)
    return render(request, 'blogger/blogHome.html', context)


def blogPost(request, slug):
    post = Post.objects.filter(slug=slug).first()
    post.views = post.views + 1
    post.save()

    comments = BlogComment.objects.filter(post=post)
    replies = BlogComment.objects.filter(post=post).exclude(parent=None) #Retrieves all replies to comments (assuming replies have a parent field referring to the parent comment).
    replyDict = {}
    # print(replies)
    # print(comments)
    for reply in replies:
        if reply.parent.sno not in replyDict.keys():
            #If the parent comment's sno is not in replyDict, add it as a key with a list containing the reply.
            replyDict[reply.parent.sno] = [reply]
        else:
            # If the sno is already in replyDict, append the reply to the list associated with that sno.
            replyDict[reply.parent.sno].append(reply)
    context = {'post': post, 'comments': comments, 'user': request.user, 'replyDict': replyDict}
    return render(request, 'blogger/blogPost.html', context)


def postComment(request):
    if request.method == 'POST':
        comment = request.POST.get('comment')
        user = request.user
        postSno = request.POST.get('postSno')
        post = Post.objects.get(sno=postSno)
        parentSno = request.POST.get('parentSno')
        if parentSno=='':
            comment = BlogComment(comment=comment, user=user, post=post)
            comment.save()
            messages.success(request, "Your comment has been posted successfully")
        else:
            parent= BlogComment.objects.get(sno=parentSno)
            comment = BlogComment(comment=comment, user=user, post=post, parent=parent)
            comment.save()
            messages.success(request, "Your reply has been posted successfully")
        return redirect(f"/blog/{post.slug}")
