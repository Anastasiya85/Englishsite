from django.urls import path
from . import views

urlpatterns = [
   # path('',views.post_category, name = 'post_category'),
    path('', views.post_index, name='post_index'),
    path("<category>/", views.post_category, name='post_category'),
    path('',views.post_subcategory,name = 'post_subcategory')
]
