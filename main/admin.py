from django.contrib import admin
from main.models import Post
from guardian.admin import GuardedModelAdmin

# Old way:
#class AuthorAdmin(admin.ModelAdmin):
#    pass

# With object permissions support
class PostAdmin(GuardedModelAdmin):
    pass

admin.site.register(Post, PostAdmin)
