from django.core.validators import FileExtensionValidator
from django.db import models


class AuthUser(models.Model):
    """
    Модель пользователя на платформе
    """
    email = models.EmailField(max_length=150, unique=True)
    join_date = models.DateTimeField(auto_now_add=True)
    country = models.CharField(max_length=30, blank=True, null=True)
    city = models.CharField(max_length=30, blank=True, null=True)
    bio = models.TextField(max_length=2000, blank=True, null=True)
    display_name = models.CharField(max_length=50, blank=True, null=True)
    avatar = models.ImageField(
        upload_to='',
        blank=True,
        null=True,
        validators=[FileExtensionValidator(allowed_extensions=['jpg '])]
    )

    def __str__(self):
        return self.email

    @property
    def is_authenticated(self):
        """
        Всегда возвращает True.
        Это способ узнать, был ли пользователь аутентифицирован.
        """
        return True


class Follower(models.Model):
    """
    Модель подписчиков и подписок
    """
    user = models.ForeignKey(AuthUser, on_delete=models.CASCADE, related_name='owner')
    subscriber = models.ForeignKey(AuthUser, on_delete=models.CASCADE, related_name='subscriber')

    def __str__(self):
        return f'{self.subscriber} подписан на {self.user}'
