from django.contrib import admin
from .models import *


@admin.register(AuthUser)
class AuthUserAdmin(admin.ModelAdmin):
    list_display = ('id', 'email', 'display_name', 'join_date')
    list_display_links = ('email', )


@admin.register(SocialLink)
class SocialLinkAdmin(admin.ModelAdmin):
    list_display = ('user', 'link')
