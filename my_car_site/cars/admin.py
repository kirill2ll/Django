from django.contrib import admin
from .models import Car, Review
# Register your models here.

class CarAdmin(admin.ModelAdmin):
    # order of the fields
    # fields = ['year','brand']

    # labels for the fields
    fieldsets = (
        ('Car Info', {
            'fields': ('year', 'brand'),
        }),
    )

admin.site.register(Car, CarAdmin)
admin.site.register(Review)