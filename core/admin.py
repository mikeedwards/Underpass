from django.contrib import admin
from inline_ordering.admin import OrderableStackedInline
from models import Kit, Level, Bridge, PostType, LevelPost, LevelPlank, \
    Post, Plank

class PostTypeAdmin(admin.ModelAdmin):
    pass

class PostAdmin(admin.ModelAdmin):
    pass
class PostInline(OrderableStackedInline):
    model = Post

class PlankAdmin(admin.ModelAdmin):
    pass
class PlankInline(OrderableStackedInline):
    model = Plank

class LevelPostAdmin(admin.ModelAdmin):
    pass
class LevelPostInline(OrderableStackedInline):
    model = LevelPost

class LevelPlankAdmin(admin.ModelAdmin):
    pass
class LevelPlankInline(OrderableStackedInline):
    model = LevelPlank

class BridgeAdmin(admin.ModelAdmin):
    inlines = (PostInline, PlankInline)

class LevelAdmin(admin.ModelAdmin):
    inlines = (LevelPostInline, LevelPlankInline)
class LevelInline(OrderableStackedInline):
    model = Level

class KitAdmin(admin.ModelAdmin):
    inlines = (LevelInline, )

admin.site.register(PostType, PostTypeAdmin)
admin.site.register(Post, PostAdmin)
admin.site.register(Plank, PlankAdmin)
admin.site.register(LevelPost, LevelPostAdmin)
admin.site.register(LevelPlank, LevelPlankAdmin)
admin.site.register(Bridge, BridgeAdmin)
admin.site.register(Level, LevelAdmin)
admin.site.register(Kit, KitAdmin)