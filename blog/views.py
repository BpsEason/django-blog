from django.shortcuts import render, get_object_or_404
from django.core.paginator import Paginator
from .models import Post

def post_list(request):
    posts = Post.objects.all().order_by('-created_at')
    paginator = Paginator(posts, 10)  # 每頁 10 篇文章
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request, 'blog/post_list.html', {'page_obj': page_obj})

def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    return render(request, 'blog/post_detail.html', {'post': post})