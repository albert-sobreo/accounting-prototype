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

class JournalAdmin(admin.ModelAdmin):
    list_display = ('code', 'date')

class JournaEntriesAdmin(admin.ModelAdmin):
    list_display = ('journal')

# Register your models here.

admin.site.register(Account_Group, AccountGroupAdmin)
admin.site.register(Account_Sub_Group, AccountSubGroupAdmin)
admin.site.register(Child_Account, ChildAccountAdmin)
admin.site.register(Party, PartyAdmin)
admin.site.register(Inventory_Item, InventoryItemAdmin)
admin.site.register(Journal, JournalAdmin)
admin.site.register(Journal_Entries)