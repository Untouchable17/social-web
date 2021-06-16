from django.contrib import admin

from social.models import Post, UserProfile, Comment


class PostAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('title',)}


admin.site.register(Post, PostAdmin)
admin.site.register(UserProfile)
admin.site.register(Comment)
