from django.db import models
from django.contrib.auth.models import User
from ckeditor_uploader.fields import RichTextUploadingField

class Category(models.Model):
    name = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name_plural = "Blog Categories"


class Tag(models.Model):
    name = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name_plural = "Blog Tags"


class BlogPost(models.Model):
    title = models.CharField(max_length=200)
    content = RichTextUploadingField()  # CKEditor
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True)
    tags = models.ManyToManyField(Tag, blank=True)
    date_published = models.DateTimeField(auto_now_add=True)
    published_by = models.ForeignKey(User, on_delete=models.CASCADE)
    thumbnail = models.ImageField(upload_to='thumbnails/')

    class Meta:
        ordering = ['-date_published']
        verbose_name_plural = "Blog Posts"

    def __str__(self):
        return self.title


class Partner(models.Model):
    name = models.CharField(max_length=200)
    full_name = models.CharField(max_length=300, blank=True, null=True)
    description = models.TextField()
    website = models.URLField(blank=True, null=True)
    logo = models.ImageField(upload_to='partners/logos/', blank=True, null=True)

    def __str__(self):
        return self.name
    
class ManagementTeamMember(models.Model):
    name = models.CharField(max_length=200)
    position = models.CharField(max_length=200)
    bio = models.TextField()
    photo = models.ImageField(upload_to='management_team/photos/', blank=True, null=True)

    def __str__(self):
        return self.name