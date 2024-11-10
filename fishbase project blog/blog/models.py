from django.db import models
from django.utils.text import slugify


# Category
class Category(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self) :
        return self.name
#post
class Post(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    img_url = models.ImageField(null=True, blank=True, upload_to='images/')
    created_at = models.DateTimeField(auto_now_add=True)
    slug = models.SlugField(unique=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super().save(*args, **kwargs)

    def __str__(self) :
        return self.title


class AboutUs(models.Model):
    content = models.TextField()

    


class Contact(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Message from {self.name} ({self.email})"


