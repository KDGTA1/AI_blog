from django.shortcuts import get_object_or_404, redirect, render
from django.urls import reverse

from .models import Post


def post_list(request):
    """公開中の記事一覧"""
    posts = Post.objects.filter(is_published=True)
    return render(request, "blog/post_list.html", {"posts": posts})


def post_detail(request, pk: int):
    """記事詳細"""
    post = get_object_or_404(Post, pk=pk, is_published=True)
    return render(request, "blog/post_detail.html", {"post": post})


def post_create(request):
    """シンプルな記事作成ビュー"""
    if request.method == "POST":
        title = request.POST.get("title", "").strip()
        content = request.POST.get("content", "").strip()
        is_published = request.POST.get("is_published") == "on"

        if title and content:
            post = Post.objects.create(
                title=title,
                content=content,
                is_published=is_published,
            )
            return redirect(reverse("blog:detail", args=[post.pk]))

    return render(request, "blog/post_form.html")


def post_edit(request, pk: int):
    """記事編集ビュー"""
    post = get_object_or_404(Post, pk=pk)

    if request.method == "POST":
        title = request.POST.get("title", "").strip()
        content = request.POST.get("content", "").strip()
        is_published = request.POST.get("is_published") == "on"

        if title and content:
            post.title = title
            post.content = content
            post.is_published = is_published
            post.save()
            return redirect(reverse("blog:detail", args=[post.pk]))

    return render(request, "blog/post_form.html", {"post": post})
