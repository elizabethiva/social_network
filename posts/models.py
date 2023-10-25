from django.db import models
from users.models import User

class Post(models.Model):
    content = models.TextField()
    user = models.ForeignKey(
        User,
        on_delete=models.RESTRICT,
        related_name="posts",
    )

    liked = models.ManyToManyField(User, blank=True, related_name="likes")

    def __str__(self):
        return f"Post by {self.user}: {self.content}"
    
    class Meta:
        db_table = "posts"


class Like(models.Model):
    """
    This model is used to leave likes on Posts
    """

    profile = models.ForeignKey(User, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)

    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.profile} liked {self.post}"