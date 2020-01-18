# Register your models here.
from django.conf import settings
from django.contrib import admin

from .models import Tenant, Room, Journal


@admin.register(Tenant)
class TenantAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'date_of_birth', 'phone')
    search_fields = ('first_name', 'last_name', 'phone', 'date_of_birth')
    list_filter = ('date_of_birth', 'last_name')


@admin.register(Room)
class RoomAdmin(admin.ModelAdmin):
    list_display = ('number', 'maximum_guest', 'owner', 'room_status')
    actions = ['on_delete', ]

    def on_delete(self, request, queryset):
        queryset.update(room_status=Room.FREE)
    on_delete.short_description = "Mark selected room as free"


@admin.register(Journal)
class JournalAdmin(admin.ModelAdmin):
    list_display = ('created', 'room', 'guests_cnt', 'is_kept')
