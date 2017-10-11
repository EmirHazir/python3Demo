from django.shortcuts import render, HttpResponse, get_object_or_404
from .models import Post


def post_index(req):
    _post = Post.objects.all()
    return render(req, 'post/index.html', {'posts': _post})


def post_detail(req, id):
    _post = get_object_or_404(Post, id=id)
    context= {
        'post' : _post,
    }
    return render(req, 'post/detail.html', context)


def post_update(req):
    return HttpResponse('update page')


def post_create(req):
    return HttpResponse('create page')


def post_delete(req):
    return HttpResponse('delete page')
