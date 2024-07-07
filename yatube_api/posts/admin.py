from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import User

from posts.models import Comment, Follow, Group, Post


@admin.register(Group)
class GroupAdmin(admin.ModelAdmin):
    list_display = (
        'title',
        'description',
        'slug',
    )
    list_display_links = ('title',)
    search_fields = ('title',)


class CommentInline(admin.StackedInline):
    model = Comment
    extra = 0


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    inlines = (CommentInline,)
    list_display = (
        'text',
        'pub_date',
        'author',
        'group',
    )
    list_editable = ('group',)
    search_fields = ('text',)
    list_filter = ('author', 'group')
    list_display_links = ('text',)
    list_select_related = ('author', 'group')


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = (
        'text',
        'post',
        'author',
        'created',
    )
    search_fields = ('text',)
    list_filter = ('author', 'post')
    list_display_links = ('text',)
    list_select_related = ('author', 'post')


@admin.register(Follow)
class FollowAdmin(admin.ModelAdmin):
    list_display = ('user', 'following')
    search_fields = ('user__username',)
    list_filter = ('user', 'following')
    list_display_links = ('user',)
    list_select_related = ('user', 'following')


class FollowInline(admin.StackedInline):
    model = Follow
    extra = 0
    fk_name = 'user'


class UserAdmin(UserAdmin):
    inlines = (FollowInline,)


admin.site.unregister(User)
admin.site.register(User, UserAdmin)
