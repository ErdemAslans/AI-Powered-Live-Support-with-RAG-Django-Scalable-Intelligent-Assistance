from django.db import models
from django.contrib.auth.models import User
from autoslug import AutoSlugField
from tinymce import models as tinymce_models

class BlogModel(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    slug = AutoSlugField(populate_from = 'title',unique=True)
    title = models.CharField(max_length=200)
    cover_image = models.ImageField(upload_to='blog_images/')
    description = tinymce_models.HTMLField(blank=True, null=True)
    description2 = tinymce_models.HTMLField(blank=True, null=True)
    is_active = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

