from django.contrib import admin
from .models import Post, Group, Follow, Comment


class FollowAdmin(admin.ModelAdmin):
    list_display = ("user", "following")
    empty_value_display = "-пусто-"


class GroupAdmin(admin.ModelAdmin):
    list_display = ("pk", "title", "slug", "description")
    exclude = ('slug',)
    empty_value_display = "-пусто-"


class PostAdmin(admin.ModelAdmin):
    list_display = ("pk", "group", "text", "pub_date", "author")
    search_fields = ("author", "group", "text")
    list_filter = ("group", "pub_date",)
    empty_value_display = "-пусто-"


class CommentAdmin(admin.ModelAdmin):
    list_display = ("pk", "author", "text", "created", "post",)
    search_fields = ("author", "post", "text")
    list_filter = ("author", "created",)
    empty_value_display = "-пусто-"


admin.site.register(Post, PostAdmin)
admin.site.register(Group, GroupAdmin)
admin.site.register(Follow, FollowAdmin)
admin.site.register(Comment, CommentAdmin)

