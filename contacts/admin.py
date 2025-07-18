from django.contrib import admin
from .models import Contact 

# Register your models here.

class ContactAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'email', 'phone', "listing", 'contact', "user_id")
    list_display_links = ('id', 'name')
    search_fields = ('name', 'email', 'phone')
    list_per_page = 25
    
admin.site.register(Contact, ContactAdmin)
# Register the Contact model with the admin site using the ContactAdmin configuration


