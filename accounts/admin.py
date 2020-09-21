from django.contrib import admin
from .models import User
from django.contrib.auth.admin import UserAdmin


class AccountAdmin(UserAdmin):
    list_display = ('email', 'is_admin', 'is_staff', 'is_superuser', 'is_active', 'created_at', 'last_login',)
    search_fields = ('email',)
    readonly_fields = ('created_at', 'last_login')

    filter_horizontal = ()
    list_filter = ()
    ordering = ('email',)
    fieldsets = (
        (None,
         {'fields': ('email', 'password')}),
        ('Permissions', {'fields': ('is_admin', 'is_staff', 'is_superuser',)}),
    )


admin.site.register(User, AccountAdmin)