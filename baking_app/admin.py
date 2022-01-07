from django.contrib import admin

from baking_app.models import Bake, Category, Images, Step

# Register your models here.
admin.site.register(Category)
admin.site.register(Bake)
admin.site.register(Images)
admin.site.register(Step)
