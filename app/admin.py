from django.contrib import admin
from .models import *

class AccountGroupAdmin(admin.ModelAdmin):
    list_display = ('code', 'name')

class AccountSubGroupAdmin(admin.ModelAdmin):
    list_display = ('code', 'name')

class ChildAccountAdmin(admin.ModelAdmin):
    list_display = ('code', 'name')

class PartyAdmin(admin.ModelAdmin):
    list_display = ('name', 'type')

class InventoryItemAdmin(admin.ModelAdmin):
    list_display = ('code', 'name')

# Register your models here.

admin.site.register(Account_Group, AccountGroupAdmin)
admin.site.register(Account_Sub_Group, AccountSubGroupAdmin)
admin.site.register(Child_Account, ChildAccountAdmin)
admin.site.register(Party, PartyAdmin)
admin.site.register(Inventory_Item, InventoryItemAdmin)