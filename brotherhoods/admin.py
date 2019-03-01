from django.contrib import admin
from . models import Brotherhood


class BrotherhoodAdmin(admin.ModelAdmin):
    readonly_fields = ('jump_order',)

admin.site.register(Brotherhood, BrotherhoodAdmin)
