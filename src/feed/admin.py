from django.contrib import admin
from .models import Post, Follow

admin.site.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'image', 'caption', 'created_at')
    search_fields = ('user__username', 'caption')
    list_filter = ('created_at',)
    ordering = ('-created_at',)
    
admin.site.register(Follow)
class FollowAdmin(admin.ModelAdmin):
    list_display = ('follower', 'following', 'created_at')
    search_fields = ('follower__username', 'following__username')
    list_filter = ('created_at',)
    ordering = ('-created_at',)
