from django.contrib import admin
from .models import Email, Tag, UserProfile

admin.site.register(Tag)


#class EmailAdmin(admin.ModelAdmin):
    #prepopulated_fields = {"slug": ("title",)}
    #exclude = ('timestamp',)

#admin.site.register(Email, EmailAdmin)
admin.site.register(Email)
admin.site.register(UserProfile)