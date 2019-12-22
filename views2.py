from django.shortcuts import render, get_object_or_404
from .models import Post, Category, Tag
from comments.forms import CommentForm
import markdown
from django.contrib.auth.models import User


def index(request):
    post_list = Post.objects.all().order_by('-created_time')
    for post in post_list:
        post.body = markdown.markdown(post.body,
                                      extensions=[
                                          'markdown.extensions.extra',
                                          'markdown.extensions.codehilite',
                                          'markdown.extensions.toc',
                                      ])
    return render(request, 'blog/index.html', context={'post_list': post_list})


def detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    post.body = markdown.markdown(post.body,
                                  extensions=[
                                      'markdown.extensions.extra',
                                      'markdown.extensions.codehilite',
                                      'markdown.extensions.toc',
                                  ])
    # 记得在顶部导入 CommentForm
    form = CommentForm()
    # 获取这篇 post 下的全部评论
    comment_list = post.comment_set.all()

    # 将文章、表单、以及文章下的评论列表作为模板变量传给 detail.html 模板，以便渲染相应数据。
    context = {'post': post,
               'form': form,
               'comment_list': comment_list,
               'comment_len': len(comment_list)
               }
    return render(request, 'blog/detail.html', context=context)


def archives(request, year, month):
    post_list = Post.objects.filter(created_time__year=year,
                                    created_time__month=month
                                    ).order_by('-created_time')
    for post in post_list:
        post.body = markdown.markdown(post.body,
                                      extensions=[
                                          'markdown.extensions.extra',
                                          'markdown.extensions.codehilite',
                                          'markdown.extensions.toc',
                                      ])
    return render(request, 'blog/index.html', context={'post_list': post_list})


def category(request, pk):
    cate = get_object_or_404(Category, pk=pk)
    post_list = Post.objects.filter(category=cate).order_by('-created_time')
    for post in post_list:
        post.body = markdown.markdown(post.body,
                                      extensions=[
                                          'markdown.extensions.extra',
                                          'markdown.extensions.codehilite',
                                          'markdown.extensions.toc',
                                      ])
    return render(request, 'blog/index.html', context={'post_list': post_list})


def Search(request):
    cate = request.GET.get('title', default='')
    post_list = Post.objects.filter(title__contains=cate).order_by('-created_time')
    for post in post_list:
        post.body = markdown.markdown(post.body,
                                      extensions=[
                                          'markdown.extensions.extra',
                                          'markdown.extensions.codehilite',
                                          'markdown.extensions.toc',
                                      ])
    return render(request, 'blog/index.html', context={'post_list': post_list})


def Register(request):
    cate = request.GET.get('title', default='')
    post_list = Post.objects.filter(title__contains=cate).order_by('-created_time')
    for post in post_list:
        post.body = markdown.markdown(post.body,
                                      extensions=[
                                          'markdown.extensions.extra',
                                          'markdown.extensions.codehilite',
                                          'markdown.extensions.toc',
                                      ])
    return render(request, 'blog/index.html', context={'post_list': post_list})


def Register(request):
    if (request.method == 'POST'):
        password=request.POST['password']
        username=request.POST['username']
        length=len(User.objects.filter(username=username))
        if length>0:
            msg="用户名不能重复"
        else:
            user=User.objects.create_superuser(username,"",password)
            msg="成功"
        return render(request, 'blog/msg.html', context={'msg': msg})
    else:
        return render(request, 'blog/register.html')
