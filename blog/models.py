from django.db import models
from django.utils import timezone


class Post(models.Model):
    """ブログ記事モデル"""

    title = models.CharField("タイトル", max_length=200)
    content = models.TextField("本文")
    created_at = models.DateTimeField("作成日時", default=timezone.now)
    updated_at = models.DateTimeField("更新日時", auto_now=True)
    is_published = models.BooleanField("公開する", default=True)

    class Meta:
        ordering = ["-created_at"]

    def __str__(self) -> str:
        return self.title
