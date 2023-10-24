from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, Group, Permission

class User(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(max_length=150, unique=True, null=False)
    first_name = models.CharField(max_length=100, null=True)
    last_name = models.CharField(max_length=100, null=True)
    
    # Добавьте related_name к полям groups и user_permissions
    groups = models.ManyToManyField(Group, related_name="user_groups")
    user_permissions = models.ManyToManyField(Permission, related_name="user_permissions")

    is_active = models.BooleanField(default=True)
    
    EMAIL_FIELD = "email"
    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []

    class Meta:
        db_table = "users"

    def __str__(self) -> str:
        if self.first_name and self.last_name:
            return f"{self.first_name} {self.last_name}"
        return self.email