from django.contrib import admin
from post.models import Category , Tag , Post ,Contact
# Register your models here.

class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("title",)}

class TagAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("title",)}

class PostAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("title",)}
    list_filter = ('status','tags','author')
    list_display = ('title','publication_date','category','author')

class ContactAdmin(admin.ModelAdmin):

    list_display = ('name' , 'email')

admin.site.register(Category , CategoryAdmin)
admin.site.register(Tag , TagAdmin)
admin.site.register(Post , PostAdmin)
admin.site.register(Contact ,ContactAdmin)