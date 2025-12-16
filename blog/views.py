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
    # セッションで既にいいねしたかチェック
    liked_posts = request.session.get("liked_posts", [])
    is_liked = pk in liked_posts
    return render(request, "blog/post_detail.html", {"post": post, "is_liked": is_liked})


def post_create(request):
    """シンプルな記事作成ビュー"""
    if request.method == "POST":
        title = request.POST.get("title", "").strip()
        content = request.POST.get("content", "").strip()
        is_published = request.POST.get("is_published") == "on"
        image = request.FILES.get("image")

        if title and content:
            post = Post.objects.create(
                title=title,
                content=content,
                is_published=is_published,
            )
            if image:
                post.image = image
                post.save()
            return redirect(reverse("blog:detail", args=[post.pk]))

    return render(request, "blog/post_form.html")


def post_edit(request, pk: int):
    """記事編集ビュー"""
    post = get_object_or_404(Post, pk=pk)

    if request.method == "POST":
        title = request.POST.get("title", "").strip()
        content = request.POST.get("content", "").strip()
        is_published = request.POST.get("is_published") == "on"
        image = request.FILES.get("image")
        delete_image = request.POST.get("delete_image") == "on"

        if title and content:
            post.title = title
            post.content = content
            post.is_published = is_published
            
            if delete_image:
                post.image.delete(save=False)
                post.image = None
            elif image:
                if post.image:
                    post.image.delete(save=False)
                post.image = image
            
            post.save()
            return redirect(reverse("blog:detail", args=[post.pk]))

    return render(request, "blog/post_form.html", {"post": post})


def post_like(request, pk: int):
    """いいね機能"""
    post = get_object_or_404(Post, pk=pk, is_published=True)
    
    # セッションで既にいいねしたかチェック
    liked_posts = request.session.get("liked_posts", [])
    
    if pk not in liked_posts:
        # いいね数を増やす
        post.likes += 1
        post.save()
        # セッションに記録
        liked_posts.append(pk)
        request.session["liked_posts"] = liked_posts
    
    return redirect(reverse("blog:detail", args=[post.pk]))
