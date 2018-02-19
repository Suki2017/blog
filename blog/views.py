import markdown
from django.shortcuts import render, get_object_or_404
from django.http import JsonResponse
# from django.http import APIView

from .models import Post, Note
from .utils import (
    get_hot_posts,
    pageonhole_count,
    generate_tag_cloud,
    friend_links,
    social_contacts,
    newest_post,
)


base_context = {
    'hot_posts': get_hot_posts(),
    'pageonholes': pageonhole_count(),
    'tagclouds': generate_tag_cloud(),
    'links': friend_links(),
    'contacts': social_contacts(),
    'new_post': newest_post(),
}


def index(request):
    posts = Post.objects.all().order_by('-created_time')
    context = {'posts': posts, 'position': 'index'}
    context.update(base_context)
    return render(request, 'blog/index.html', context=context)


def posts(request):
    posts = Post.objects.all().order_by('-created_time')
    context = {'posts': posts, 'position': 'posts'}
    context.update(base_context)
    return render(request, 'blog/index.html', context=context)


def detail(request, post_id):
    post = get_object_or_404(Post, pk=post_id)
    post.body = markdown.markdown(post.body,
                                  extensions=['markdown.extensions.extra',
                                              'markdown.extensions.codehilite',
                                              'markdown.extensions.toc',
                                              ]
                                  )
    context = {'post': post, 'position': 'posts'}
    context.update(base_context)
    return render(request, 'blog/detail.html', context=context)


def category(request, category_id):
    posts = Post.objects.filter(category_id=category_id).all()
    context = {'posts': posts, 'position': 'posts'}
    context.update(base_context)
    return render(request, 'blog/index.html', context=context)


def add_thank(request, post_id):
    post = get_object_or_404(Post, pk=post_id)
    post.thanks += 1
    post.save()
    return JsonResponse({'OK': 'success', 'count': post.thanks}, status=200)


def edit_post(request):
    return render(request, 'blog/edit_post.html')


def notes(request):
    ns = Note.objects.all()
    context = {'posts': ns, 'position': 'notes'}
    context.update(base_context)
    return render(request, 'blog/notes.html', context=context)


def thinks(request):
    ns = Note.objects.all()
    context = {'posts': ns, 'position': 'thinks'}
    context.update(base_context)
    return render(request, 'blog/notes.html', context=context)


def message(request):
    ns = Note.objects.all()
    context = {'posts': ns, 'position': 'message'}
    context.update(base_context)
    return render(request, 'blog/notes.html', context=context)


def about(request):
    ns = Note.objects.all()
    context = {'posts': ns, 'position': 'about'}
    context.update(base_context)
    return render(request, 'blog/notes.html', context=context)






