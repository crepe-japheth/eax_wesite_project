from django.contrib import admin
from django.contrib.auth.models import Group
from .models import BlogPost, Category, Tag, Partner, ManagementTeamMember
from django.contrib.auth.models import User
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django import forms


class CustomUserAdmin(BaseUserAdmin):
    fieldsets = (
        (None, {'fields': ('username', 'password')}),
        ('Personal info', {'fields': ('first_name', 'last_name', 'email')}),
        ('Status', {'fields': ('is_active', 'is_staff', 'is_superuser', 'user_permissions')}),
        ('Important dates', {'fields': ('last_login', 'date_joined')}),
    )

admin.site.unregister(User)
admin.site.register(User, CustomUserAdmin)



@admin.register(BlogPost)
class BlogPostAdmin(admin.ModelAdmin):
    list_display = ("title", "category", "published_by", "date_published")
    list_filter = ("category", "published_by", "date_published")
    search_fields = ("title", "content")
    date_hierarchy = "date_published"
    ordering = ("-date_published",)
    autocomplete_fields = ["category", "tags"]
    readonly_fields = ("date_published",)

    fieldsets = (
        ("Content Info", {
            "fields": ("title", "content", "thumbnail")
        }),
        ("Classification", {
            "fields": ("category", "tags")
        }),
        ("Publishing", {
            "fields": ("published_by", "date_published")
        }),
    )

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ("name",)
    search_fields = ("name",)
    verbose_name_plural = "Categories"

@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    list_display = ("name",)
    search_fields = ("name",)


@admin.register(Partner)
class PartnerAdmin(admin.ModelAdmin):
    list_display = ("name", "full_name", "website")
    search_fields = ("name", "full_name")
    # readonly_fields = ("logo",)

@admin.register(ManagementTeamMember)
class ManagementTeamMemberAdmin(admin.ModelAdmin):
    list_display = ("name", "position")
    search_fields = ("name", "position")
    # readonly_fields = ("photo",)

admin.site.unregister(Group)