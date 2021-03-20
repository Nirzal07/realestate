from django.contrib import admin
from .models import PropertyDetails, Comment

class Arrangement(admin.ModelAdmin):
    list_display = ('id','seller', 'property_type', 'property_option', 'price', 'is_published')
    list_filter = ('seller', 'property_type', 'property_option')
    search_fields = ('seller__username', 'property_type', 'property_option')
    list_display_links = ('id', 'seller')
    list_editable = ('is_published',)

admin.site.register(PropertyDetails, Arrangement)

class CommentArrangement(admin.ModelAdmin):
    list_display = ('id','user','comment','publish')
    list_filter = ('commented_on','user','publish')
    search_fields = ('comment','user')
    list_display_links = ('id', 'comment')
    list_editable = ('publish',)

admin.site.register(Comment, CommentArrangement)
