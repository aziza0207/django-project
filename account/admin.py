from django.utils.translation import gettext_lazy as _
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from account import models


class UserAdmin(BaseUserAdmin):
    ordering = ['id']
    list_display = ['email', 'full_name']
    fieldsets = ((None, {'fields': ('email', 'password')}),
                 (_('Permissions'),
                  {'fields': (
                      'is_active',
                      'is_staff',
                      'is_superuser',

                  )}),
                 (_('Important_dates'), {'fields': ('last_login',)}))
    readonly_fields = ['last_login']
    add_fieldsets = ((None, {'fields':
                                 ('email',
                                  'password1',
                                  'password2',
                                  'full_name',
                                  'is_active',
                                  'is_staff',
                                  'is_superuser')
                             }
                      ),)


admin.site.register(models.User, UserAdmin)
