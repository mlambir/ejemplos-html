from django.contrib import admin
from main.models import Element, Example

@admin.register(Element)
class AuthorAdmin(admin.ModelAdmin):
    pass

@admin.register(Example)
class AuthorAdmin(admin.ModelAdmin):
    pass