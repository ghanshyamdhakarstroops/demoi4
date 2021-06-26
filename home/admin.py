from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import *

@admin.register(User)
class UserAdmin(UserAdmin):
	list_display = ['username', 'first_name', 'last_name', 'phone', 'email', 'is_superuser', 'is_staff']
	fieldsets = [
		(None, {'fields': ('email', 'username', 'phone', 'first_name', 'last_name', 'password',)}),
		('Permissions', {'classes': ('collapse', ), 'fields': ('is_superuser', 'is_staff', 'is_active', 'groups', 'user_permissions')})]



# Register your models here.
