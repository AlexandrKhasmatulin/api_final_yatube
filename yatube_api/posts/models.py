from django.contrib.auth import get_user_model
from django.db import models

User = get_user_model()


class Group(models.Model):
    title = models.CharField('Название сообщества', max_length=200)
    slug = models.SlugField('Slug', unique=True)
    description = models.TextField('Описание сообщества')

    class Meta:
        verbose_name = 'сообщество'
        verbose_name_plural = 'Сообщества'

    def __str__(self):
        return self.title[:30]


class Follow(models.Model):
    user = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='following',
        verbose_name='Пользователь, оформивший подписку')
    following = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='followers',
        verbose_name='Подписка пользователя')

    class Meta:
        verbose_name = 'подписка'
        verbose_name_plural = 'Подписки'
        constraints = [
            models.UniqueConstraint(fields=['user', 'following'],
                                    name='unique_following'),
            models.CheckConstraint(check=~models.Q(user=models.F('following')),
                                   name='following_oneself_not_allowed'),
        ]

    def __str__(self):
        return f'{self.user} подписан на {self.following}'


class Post(models.Model):
    text = models.TextField('Текст публикации')
    pub_date = models.DateTimeField('Дата публикации', auto_now_add=True)
    author = models.ForeignKey(
        User, on_delete=models.CASCADE,
        related_name='posts', verbose_name='Автор публикации'
    )
    image = models.ImageField(
        upload_to='posts/', null=True, blank=True, verbose_name='Изображение')
    group = models.ForeignKey(
        Group, on_delete=models.SET_NULL,
        related_name='posts', blank=True, null=True,
        verbose_name='Сообщество'
    )

    class Meta:
        verbose_name = 'публикация'
        verbose_name_plural = 'Публикации'
        ordering = ('pub_date',)

    def __str__(self):
        return self.text[:30]


class Comment(models.Model):
    author = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='comments',
        verbose_name='Автор комментария'
    )
    post = models.ForeignKey(
        Post, on_delete=models.CASCADE, related_name='comments',
        verbose_name='Публикация'
    )
    text = models.TextField('Текст комментария')
    created = models.DateTimeField(
        'Дата добавления', auto_now_add=True, db_index=True)

    class Meta:
        verbose_name = 'комментарий'
        verbose_name_plural = 'Комментарии'
        ordering = ('created',)

    def __str__(self):
        return self.text[:30]
