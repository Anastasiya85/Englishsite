from django.shortcuts import render
from pages.models import Post,Category,Subcategory

def post_category(request,category):
    posts = Post.objects.filter(
        categories_name_contains = category


    )
    context = {
        'category': category,
        'posts': posts,
    }
    return render(request, 'post_category.html',context)

def post_subcategory(request,subcategory):
    posts = Post.objects.filter(
        subcategories_name_contains = subcategory
    )
    context = {
        'subcategory': subcategory,
        'posts': posts}
    return render(request, 'post_subcategory.html',context)

# Create your views here.
