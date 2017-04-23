from django.contrib import admin
from blog.models import Post

class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'modify_date')
    list_filter = ('modify_date',)              #filter list
    search_fields = ('title', 'content')        #Search Fields
    prepopulated_fields = {'slug': ('title',)}  #slug fields are fiiled with each title field

admin.site.register(Post, PostAdmin)
