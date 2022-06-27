from django.contrib import admin
from apps.core.models import *
from django.utils.safestring import mark_safe


@admin.register(Unit)
class UnitAdmin(admin.ModelAdmin):
    pass

@admin.register(MainService)
class MainServiceAdmin(admin.ModelAdmin):
    def image(self, obj=None):
        if obj.pk:
            img = mark_safe("""<img style="width:240px; height:240px; object-fit: cover; object-position: center; border: 1px solid #ededed;" 
                src="{url}" width="{width}" height={height} />""".format(url = obj.image_s.url, width=240, height=240))
            return img
        else:
            return '-'

    readonly_fields = ['image']
    fields = ['image','image_l','name','index']


@admin.register(Service)
class ServiceAdmin(admin.ModelAdmin):
    pass

class ServiceInline(admin.StackedInline):
    def image(self, obj=None):
        if obj.pk:
            img = mark_safe("""<img style="width:240px; height:240px; object-fit: cover; object-position: center; border: 1px solid #ededed;" 
                src="{url}" width="{width}" height={height} />""".format(url = obj.image_s.url, width=240, height=240))
            return img
        else:
            return '-'

    model = Service
    extra = 0

    readonly_fields = ['image']
    fields = ['image','image_l','name','subtitle','price','index','unit','blank']

@admin.register(ServiceGroup)
class ServiceGroupAdmin(admin.ModelAdmin):
    inlines = [ServiceInline]


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    pass