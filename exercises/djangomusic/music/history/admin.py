from django.contrib import admin

from .models import Songs, Artist


class SongsInline(admin.TabularInline):
    model = Songs
    extra = 3


class ArtistAdmin(admin.ModelAdmin):
    fieldsets = [
        (None,               {'fields': ['artist_name']}),
        ('Date information', {'fields': ['pub_date'], 'classes': ['collapse']}),
    ]
    inlines = [SongsInline]

admin.site.register(Artist, ArtistAdmin)