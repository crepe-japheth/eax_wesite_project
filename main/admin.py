from django.contrib import admin
from django.contrib.auth.models import Group
from .models import BlogPost, Category, Tag

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

@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    list_display = ("name",)
    search_fields = ("name",)


admin.site.unregister(Group)