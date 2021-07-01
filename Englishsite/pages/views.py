from django.shortcuts import render
from pages.models import Post,Category

def post_category(request,category):
    posts = Post.object.filter(
        categories_name_contains = category


    )
    context = {
        'category': category,
        'posts': posts,
    }
    return render(request, 'post_category.html',context)

def post_subcategory(request,subcategory):
    posts = Post.object.filters(
        subcategories_name_contains = subcategory
    )
    context = {
        'subcategory': subcategory,
        'posts': posts}
    return render(request, 'post_subcategory.html',context)

# Create your views here.
