from django.contrib import admin
from .models import category

class  categoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug' : ('category_name',)}
    list_display = ('category_name','slug')

# Register your models here.
admin.site.register(category, categoryAdmin)
