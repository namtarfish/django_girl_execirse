from django.shortcuts import render
from .models import Post
from django.utils import timezone
from .forms import PostForm

# Create your views here.
def post_list(request):
    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    return render(request, 'blog/post_list.html', {'posts': posts})

def post_detail(request, pk):
    posts = Post.objects.filter(pk=pk)
    return render(request, 'blog/post_list.html', {'posts': posts})
