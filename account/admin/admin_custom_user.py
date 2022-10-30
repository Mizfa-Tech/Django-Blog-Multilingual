from django.contrib import admin
from django.contrib.auth import get_user_model


@admin.register(get_user_model())
class CustomUserAdmin(admin.ModelAdmin):
    list_display = ('username', 'email', 'first_name', 'last_name', 'is_active', 'is_staff', 'is_superuser')
    search_fields = ('username', 'email', 'first_name', 'last_name')


    fieldsets = (
        ("Personal", {'fields': ('username', "password", 'email', 'first_name', 'last_name',)}),
        ("Permission", {'fields': ('is_active', 'is_staff', 'is_superuser')}),
    )

    add_fieldsets = (
        ("Personal", {'fields': ('username', "password", 'email', 'first_name', 'last_name',)}),
        ("Permission", {'fields': ('is_active', 'is_staff', 'is_superuser')}),
    )
