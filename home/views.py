from django.shortcuts import render
from django.utils import timezone
from blog.models import Post

# Create your views here.

def home_list(request):
    posts = Post.objects.order_by('-created_date')[0]
    return render(request, 'home/home_list.html', {'posts':posts})