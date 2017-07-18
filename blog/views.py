from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from .models import Blog

# Create your views here.

# this is basically the home page where 
# all the blogs are shown
def blog_list(request):
    queryset = Blog.objects.all();

    context = {
        "content" : queryset[0].content,
        "objects" : queryset,
        "title" : "Home"
    }
    return render(request, "blog_list.html", context)
    
def blog_detail(request, id=None):
    blog = get_object_or_404(Blog, id=id)

    context = {
        "obj" : blog,
    }
    return render(request, "blog_detail.html", context)

def contact_me(request):
    return render(request, "contact_me.html")

# i don't know if i'll actually needs these
# i'll just do these through the admin view 
'''
    def blog_update(request):
    def blog_delete(request):
'''
