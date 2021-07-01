from django.db import models
from django.contrib.auth.models import User
from django.template.defaultfilters import slugify

class Category(models.Model):
    name = models.CharField(max_length = 20)

    def __str__(self):
        return self.name

class Subcategory(models.Model):
    name = models.CharField(max_length=40)
    category = models.ForeignKey('Category',  on_delete = models.CASCADE)

    def __str__(self):
        return self.name


class Post(models.Model):
    title = models.CharField(max_length = 255)
    body = models.TextField()
    subcategories = models.ManyToManyField('Subcategory', related_name = 'posts')
    image = models.FileField(blank = True)

    def __str__(self):
        return self.title

def get_image_filename(instance,filename):
    title = instance.post.title
    slug = slugify(title)
    return "post_images/%s-%s" % (slug, filename)

class Images(models.Model):
    post = models.ForeignKey(Post,default = None, on_delete=models.CASCADE)
    image = models.FileField(upload_to = 'images/')

    def __str__(self):
        return self.post.title
