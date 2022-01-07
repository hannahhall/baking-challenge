from django.contrib import admin

from baking_app.models import Bake, Category, Image, Step


class ImageInline(admin.StackedInline):
    """Add images inline while adding steps
    """
    model = Image
    extra = 1


class StepAdmin(admin.ModelAdmin):
    """Customize Step Admin"""
    model = Step
    inlines = [ImageInline]


# Register your models here.
admin.site.register(Category)
admin.site.register(Bake)
admin.site.register(Image)
admin.site.register(Step, StepAdmin)
