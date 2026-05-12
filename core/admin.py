from django.contrib import admin
from .models import *

# Register all models
admin.site.register(Service)
admin.site.register(Portfolio)
admin.site.register(Testimonial)
admin.site.register(PricingPackage)
admin.site.register(BlogPost)

# Special registration for CompanyInfo (Singleton)
@admin.register(CompanyInfo)
class CompanyInfoAdmin(admin.ModelAdmin):
    def has_add_permission(self, request):
        return False if CompanyInfo.objects.exists() else True
# Register your models here.
