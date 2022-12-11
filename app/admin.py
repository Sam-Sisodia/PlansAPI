from django.contrib import admin

# Register your models here.

from .models import *

admin.site.register(UserPlans)
admin.site.register(User)
@admin.register(Plan)
class PlanAdmin(admin.ModelAdmin):
    list_display= ['name','price','create_at','update_at','plantype','Company']