from django.contrib import admin
from django.contrib.auth.models import User

from .models import Post, Tag, Category, FriendLink, Contact, Comment
from .models import Note


admin.site.register(Post)
admin.site.register(Tag)
admin.site.register(Category)
admin.site.register(FriendLink)
admin.site.register(Contact)
admin.site.register(Comment)
admin.site.register(Note)
