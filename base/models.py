from django.db import models
from django.utils import timezone
from django.utils.text import slugify
from django.urls import reverse
from ckeditor.fields import RichTextField


class Project(models.Model):
    name = models.CharField(max_length=200, null=True)
    description = RichTextField(blank=True, null=True)
    online = models.URLField(max_length=200, null=True, blank=True)  
    github = models.URLField(max_length=200, null=True, blank=True)
    image = models.ImageField(null=True, upload_to='images/')
    date_completed = models.DateField(null=True, blank=True) 
    project_type = models.CharField(max_length=100, null=True, blank=True)  
    security_tools = models.CharField(max_length=200, null=True, blank=True)  

    def __str__(self):
        return self.name

class Certification(models.Model):
    name = models.CharField(max_length=100)
    issuing_organization = models.CharField(max_length=100)
    date_received = models.DateField()
    description = models.TextField(blank=True, null=True)
    image = models.ImageField(null=True, upload_to='certifications/') 
    online = models.URLField(max_length=200, blank=True, null=True)

    def __str__(self):
        return self.name


class Post(models.Model):
    title = models.CharField(max_length=200)
    slug = models.SlugField(max_length=200, unique=True, blank=True)
    author = models.CharField(max_length=100)
    content = RichTextField(blank=True, null=True)
    created_at = models.DateTimeField(default=timezone.now)
    updated_at = models.DateTimeField(auto_now=True)
    image = models.ImageField(upload_to='post_images/', blank=True, null=True)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super().save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse('post_detail', kwargs={'slug': self.slug})
    

    def __str__(self):
        return self.title
    
    
class Skill(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True, null=True)
    proficiency = models.IntegerField(help_text="Proficiency level from 1 to 10", default=5)

    def __str__(self):
        return self.name