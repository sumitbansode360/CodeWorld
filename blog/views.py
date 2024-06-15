from django.shortcuts import render,get_object_or_404,HttpResponse,redirect
from .models import *
from django.db.models import Q
from django.contrib import messages


# Create your views here.

def blog(request):
    blogs = Blog.objects.all().order_by('-views_count')
    context = {'allPosts':blogs}
    return render(request,'blog/index.html',context)

def blogpost(request,slug):
    blog = get_object_or_404(Blog, slug=slug) 
    blog.views_count = blog.views_count + 1
    blog.save()
    comments = BlogComment.objects.filter(post=blog,parent=None).order_by('-timestamp')  # Fetch comments for the blog post
    replies =  BlogComment.objects.filter(post=blog).exclude(parent=None)
    replyDict = {}
    for reply in replies:
        if reply.parent.sno not in replyDict.keys():
            replyDict[reply.parent.sno] = [reply]
        else:
            replyDict[reply.parent.sno].append(reply)
    context = {'blog':blog,'comments': comments,'user':request.user,'replyDict':replyDict}
    return render(request,'blog/blogpost.html',context)

def search(request):
    blog = Blog.objects.all()
    if request.GET.get('search'):
        search = request.GET.get('search')
        search_blog = blog.filter(
            Q(title__icontains=search)|
            Q(author__icontains=search)|
            Q(headings__icontains=search)|
            Q(timeStamp__icontains=search)|
            Q(content__icontains=search)
        )
        if len(search_blog) == 0:
            search_not_found = True
            context = {'nodata':search_not_found}
            return render(request,'blog/search.html',context)
        context = {'results':search_blog}
    return render(request,'blog/search.html',context)

# def like(request,slug):
#     blog = get_object_or_404(Blog, slug=slug) 
#     blog.like = blog.like + 1
#     blog.save()

def postComment(request):
    if request.method == 'POST':
        comment_text = request.POST.get('comment')
        user = request.user
        post_id = request.POST.get('postSno')
        parent_sno = request.POST.get('parentSno', None)

        try:
            post = Blog.objects.get(id=post_id)
        except Blog.DoesNotExist:
            messages.error(request, "Post not found.")
            return redirect('/')

        if parent_sno:
            try:
                parent = BlogComment.objects.get(sno=parent_sno)
                comment = BlogComment(comment=comment_text, user=user, post=post, parent=parent)
            except BlogComment.DoesNotExist:
                messages.error(request, "Parent comment not found.")
                return redirect(f"/blog/{post.slug}")
        else:
            comment = BlogComment(comment=comment_text, user=user, post=post)

        comment.save()
        messages.success(request, "Comment posted!")

    return redirect(f"/blog/{post.slug}")

