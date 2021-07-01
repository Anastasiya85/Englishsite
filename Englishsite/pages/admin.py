from django.contrib import admin

from pages.models import Post, Category,Subcategory

class PostAdmin (admin.ModelAdmin):
    pass

class CategoryAdmin(admin.ModelAdmin):
    pass

class SubcategoryAdmin(admin.ModelAdmin):
    pass
admin.site.register(Post,PostAdmin)
admin.site.register(Category,CategoryAdmin)
admin.site.register(Subcategory,SubcategoryAdmin)
# Register your models here.
