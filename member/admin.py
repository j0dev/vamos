from django.contrib import admin
from member.models import Member, University


@admin.register(Member)
class UserAdmin(admin.ModelAdmin):
    list_display = ['username', 'email', 'createdAt', 'is_active']
    list_display_links = ['username', 'email']
    list_editable = ['is_active']
    list_per_page = 20


@admin.register(University)
class UniversityAdmin(admin.ModelAdmin):
    list_display = ['name']
    list_display_links = ['name']
    list_per_page = 20


