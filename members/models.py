from django.db import models
from django.utils.text import slugify
from django.contrib.auth import get_user_model
from django.contrib.contenttypes.fields import GenericRelation
from django.shortcuts import reverse
from django_resized import ResizedImageField
from hitcount.models import HitCountMixin, HitCount
from taggit.managers import TaggableManager

# Create your models here.

User = get_user_model()

class Author(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    fullname = models.CharField(max_length=40, blank=True, null=True)
    slug = models.SlugField(max_length=400, unique=True, blank=True)
    bio = models.TextField(blank=True, null=True)
    points = models.IntegerField(default=0)
    profile_pic = ResizedImageField(size=[50, 80], quality=100, upload_to="authors", default= None, null=True)
    
    def __str__(self):
        return self.fullname
    
    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.fullname)
        super(Author, self).save(*args, **kwargs)

class Reply(models.Model):
    user = models.ForeignKey(Author, on_delete=models.CASCADE)
    content = models.TextField()
    date = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.content[:100]
    
    class Meta:
        verbose_name_plural = "Replies"
    
class Comment(models.Model):
    user = models.ForeignKey(Author, on_delete=models.CASCADE)
    content = models.TextField()
    date = models.DateTimeField(auto_now_add=True)
    replies = models.ManyToManyField(Reply, blank=True)
    
    def __str__(self):
        return self.content[:100]
    
    def num_reply(self):
        return self.replies.count()    
        
class Category(models.Model):
    title = models.CharField(max_length=50)
    slug = models.SlugField(max_length=400, unique=True, blank=True)
    description = models.TextField(default="Description")
    
    class Meta:
        verbose_name_plural = "Categories"
        
    def __str__(self):
        return self.title
    
    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super(Category, self).save(*args, **kwargs)
        
    def get_url(self):
        return reverse("posts", kwargs={"slug": self.slug})
    
    @property
    def get_post_count(self):
        return Post.objects.filter(categories=self,approved=True).count()
        
    @property
    def get_last_post(self):
        return Post.objects.filter(categories=self,approved=True).latest("date")

class Post(models.Model):
    title = models.CharField(max_length=200)
    slug = models.SlugField(max_length=400, unique=True, blank=True)
    user = models.ForeignKey(Author, on_delete=models.CASCADE)
    content = models.TextField()
    categories = models.ManyToManyField(Category)
    date = models.DateTimeField(auto_now_add=True)
    hitcount_generic = GenericRelation(HitCount, object_id_field='object_pk', related_query_name='hit_count_generic_relation')
    tags = TaggableManager()
    comments = models.ManyToManyField(Comment, blank=True)
    approved = models.BooleanField(default=False)
    
    
    def __str__(self):
        return self.title   

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super(Post, self).save(*args, **kwargs)
        
    def get_url(self):
        return reverse("details", kwargs={"slug": self.slug})
    
    @property 
    def num_comments(self):
        ans = 0
        for comment in self.comments.all():
            ans += comment.num_reply()
            ans += 1
        return ans
    
    @property
    def last_reply(self):
        return self.comments.latest("date")
    

